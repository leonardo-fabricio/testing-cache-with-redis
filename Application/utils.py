from django.core.cache import cache  
class CacheControl():
      def __init__(self, offer_id):
            self.ATTR_CACHE_PRODUCT = "product_cache_key_"
            self.TIME_CACHE = 60*60*24
            self.OFFER_ID = offer_id

      def get_or_create_cache(self, **params):
            "get or create cache for offer"
            key = self.generate_key()
            attr = cache.get(key)
            if attr:
                  print("acessei a cache")
                  return attr.get("values")
            cache.set(key, {"values": params.get("values")}, self.TIME_CACHE)
            print("não acessei a cache")
            return params.get("values")
      
      def delete_cache(self):
            if self.get_cache():
                  key = self.generate_key()
                  cache.delete(key) 
            
      def generate_key(self):
            return "{}{}".format(self.ATTR_CACHE_PRODUCT, self.OFFER_ID)

      def get_cache(self):
            key = self.generate_key()
            attr = cache.get(key)
            return attr.get("values") if attr != None else None
            
      def create_cache(self, values):
            key = self.generate_key()
            cache.set(key, {"values": values}, self.TIME_CACHE)
            return values