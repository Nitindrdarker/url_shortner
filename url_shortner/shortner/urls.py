from django.urls import path
from .views import create_short_url_view, redirect_url

urlpatterns = [
    path('shorten/', create_short_url_view),
    path('<str:code>/', redirect_url),
]