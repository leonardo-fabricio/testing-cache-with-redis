
from django.utils.decorators import method_decorator
from Application.serializer import ModelTestProductSerializer
from Application.utils import *
from .models import *
from rest_framework.response import Response
from rest_framework import viewsets,generics,status
from django.core.cache import cache 
from rest_framework.decorators import api_view


class ProductViewSet(viewsets.ViewSet):
    # With cookie: cache requested url for each user for 2 hours
    def list(self, request, format=None):
        content = {
            'products': ModelTestProduct.objects.all().values("id","name","description", "price")
        }
        return Response(verify_or_create_cache(request.get_full_path(), content))

class DetailProduct(generics.RetrieveAPIView):
      lookup_field = "pk"
      queryset = ModelTestProduct.objects.all()
      serializer_class = ModelTestProductSerializer

      def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        res = verify_or_create_cache(instance.pk,request.get_full_path() ,serializer.data) 
        return Response(res.get("values"))

@api_view(('GET',))
def ListValuesCache(request):
      cache_attr = cache.get_many(cache.keys("*"))
      return Response(cache_attr)

@api_view(('DELETE',))
def DeleteValuesCache(request):
      cache.delete_many(cache.keys("*"))
      return Response({"detail": "clear cache successfully"})
     