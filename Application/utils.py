from django.core.cache import cache  
class CacheControl():
      """Cache control of product"""

      def __init__(self, offer_id):
            self.ATTR_CACHE_PRODUCT = "product_cache_key_" # Key default for offer
            self.TIME_CACHE = 60*60*24 # Cache time life 
            self.OFFER_ID = offer_id # Id of the offer
            self.KEY = self.generate_key()

      def get_or_create_cache(self, **params):
            "get or create cache for offer"
            attr = self.get_cache() if self.get_cache() != None else self.create_cache(params.get("values"))
            return attr
      
      def delete_cache(self):
            "delete cache for offer"
            if self.get_cache():
                  cache.delete(self.KEY) 
            
      def generate_key(self):
            "generate key for offer"
            return "{}{}".format(self.ATTR_CACHE_PRODUCT, self.OFFER_ID)

      def get_cache(self):
            "get cache for offer"
            attr = cache.get(self.KEY)
            return attr.get("values") if attr != None else None
            
      def create_cache(self, values):
            "create cache for offer"
            cache.set(self.KEY, {"values": values}, self.TIME_CACHE)
            return values