from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect

from shortner.services.rate_limiter import is_rate_limited
from rest_framework import status
from .services.cache_services import  set_original_url, get_original_url
from .models import URL
from .serializers import URLSerializer
from .services.base62 import encode
from .tasks import log_click
from celery import current_app
import uuid
from django.db.models import Count
from .serializers import URLAnalyticsSerializer

@api_view(['POST'])
def create_short_url_view(request):
    ip = request.META.get("REMOTE_ADDR")
    print(f"===============ip adderess:{ip}")
    
    if is_rate_limited(ip):
        return Response({"message":"Too many requests"}, status=status.HTTP_429_TOO_MANY_REQUESTS)
    serializer = URLSerializer(data=request.data)
    
    if serializer.is_valid():
        url = serializer.save()

        url.short_code = encode(url.id)
        url.save()
        set_original_url(url.short_code, url.original_url)
        return Response({
            "short_code": url.short_code,
            "short_url": f"http://127.0.0.1:8000/api/{url.short_code}"
        })

    return Response(serializer.errors, status=400)


def redirect_url(request, code):


    #try cache
    cache_url = get_original_url(short_code=code)
    ip = request.META.get('REMOTE_ADDR')
    if cache_url:
        print("========================cache hit, inside cache==================")
        request_id = str(uuid.uuid4())
        log_click.delay(code, ip, request_id)
        return redirect(cache_url)

    try:
        print("========================cache Miss, inside DB==================")
        url = URL.objects.get(short_code=code)

        #store in cache
        set_original_url(code, url.original_url)
        request_id = str(uuid.uuid4())
        log_click.delay(code, ip, request_id)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        print("====================errro=================")
        return JsonResponse({"error": "Not found"}, status=404)
    



@api_view(["GET"])
def url_analytics(request, code):
    try:
        url = URL.objects.annotate(
            total_clicks = Count("clickevent") # this is in serilizer, not in model
        ).get(short_code=code)
        serializer = URLAnalyticsSerializer(url)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response({"error":"Url not found"}, status=404)



@api_view(['GET'])
def top_urls(request):
    urls = URL.objects.annotate(
        total_clicks=Count('clickevent')
    ).order_by('-total_clicks')[:10]

    serializer = URLAnalyticsSerializer(urls, many=True)

    return Response(serializer.data)