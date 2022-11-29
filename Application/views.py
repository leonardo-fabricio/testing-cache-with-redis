
from django.utils.decorators import method_decorator
from Application.serializer import ModelTestProductSerializer
from Application.utils import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets,generics,status
from django.core.cache import cache 
from rest_framework.decorators import api_view

class DetailProduct(generics.RetrieveAPIView):
        lookup_field = "pk"
        queryset = ModelTestProduct.objects.all()
        serializer_class = ModelTestProductSerializer

        def retrieve(self, request, *args, **kwargs):
            cacheControl = CacheControl(self.kwargs["pk"])
            attr = cacheControl.get_cache() 
            if attr: 
                print("acessei a cache")
                return Response(attr)

            instance = self.get_object()
            serializer = self.get_serializer(instance)
            attr = cacheControl.create_cache(serializer.data)
            print("não acessei a cache")
            return Response(attr)

        


        
        

@api_view(('GET',))
def ListValuesCache(request):
      cache_attr = cache.get_many(cache.keys("*"))
      return Response(cache_attr)

@api_view(('DELETE',))
def DeleteValuesCache(request):
      cache.delete_many(cache.keys("*"))
      return Response({"detail": "clear cache successfully"})
     