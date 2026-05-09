from django.core.cache import cache
import time

RATE_LIMIT = 30 #requests
WINDOW = 10 #seconds



def is_rate_limited(ip):
    key = f"rate_limit:{ip}"
    current = cache.get(key)
    
    if current is None:
        #first request
        cache.set(key, 1, timeout=WINDOW)
        return False
    
    if current >= RATE_LIMIT:
        return True

    cache.incr(key)
    return False

