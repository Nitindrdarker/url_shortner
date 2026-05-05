from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect

from .services.cache_services import  set_original_url, get_original_url
from .models import URL
from .serializers import URLSerializer
from .services.base62 import encode

@api_view(['POST'])
def create_short_url_view(request):
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

    if cache_url:
        print("========================cache hit, inside cache==================")
        return redirect(cache_url)

    try:
        print("========================cache Miss, inside DB==================")
        url = URL.objects.get(short_code=code)

        #store in cache
        set_original_url(code, url.original_url)

        return redirect(url.original_url)
    except URL.DoesNotExist:
        print("====================errro=================")
        return JsonResponse({"error": "Not found"}, status=404)