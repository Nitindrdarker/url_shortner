from ..models import URL
from .base62 import encode

def create_short_url(original_url):
    # Check if already exists
    existing = URL.objects.filter(original_url=original_url).first()
    if existing:
        return existing

    url = URL.objects.create(original_url=original_url)

    url.short_code = encode(url.id)
    url.save(update_fields=["short_code"])

    return url