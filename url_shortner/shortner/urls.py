from django.urls import path
from .views import create_short_url_view, redirect_url, top_urls, url_analytics

urlpatterns = [
    path('shorten/', create_short_url_view),
    path('top-urls/', top_urls),
    path('<str:code>/', redirect_url),
    path('analytics/<str:code>/', url_analytics),
    
]