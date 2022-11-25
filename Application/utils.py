from django.core.cache import cache 

ATTR_CACHE_PRODUCT = "product_cache_key_"
TIME_CACHE = 60*60*24

def verify_or_create_cache(key, router, value):
      key = f"{ATTR_CACHE_PRODUCT}{key}"
      attr = cache.get(key)
      if attr:
            return attr
      
      cache.set(key, {"router" :router,  "values": value}, TIME_CACHE)
      return cache.get(key)

def del_key(key):
      try:
            key = f"{ATTR_CACHE_PRODUCT}{key}"
            cache.delete(key) 
      except Exception as e:
            return e
            
# def verify_or_create_cache(key, value=None):
#       if cache.get(key):
#             return cache.get(key)
#       cache.set(key, value)
#       return cache.get(key)