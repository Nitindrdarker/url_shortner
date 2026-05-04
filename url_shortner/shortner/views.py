from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import URL
from .serializers import URLSerializer
from .services.base62 import encode

@api_view(['POST'])
def create_short_url_view(request):
    serializer = URLSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            url = serializer.save()

            url.short_code = encode(url.id)
            url.save()
            return Response({
                "short_code": url.short_code,
                "short_url": f"http://127.0.0.1:8000/api/{url.short_code}"
            })
        except:
            return Response({"message":"Somthing wrong while creating the url"}, status=400)

        


    return Response(serializer.errors, status=400)


def redirect_url(request, code):
    try:
        url = URL.objects.get(short_code=code)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        return Response({"error": "Not found"}, status=404)