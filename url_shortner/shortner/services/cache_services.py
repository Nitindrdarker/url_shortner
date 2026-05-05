from django.core.cache import cache

CACHE_TTL = 60 * 60


def get_original_url(short_code):
    return cache.get(short_code)


def set_original_url(short_code, original_url):
    cache.set(short_code, original_url, CACHE_TTL)
