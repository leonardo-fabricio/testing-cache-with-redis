from django.db import models
from .utils import *
class ModelTestProduct(models.Model):
      name = models.CharField(max_length=255)
      description = models.TextField()
      price = models.DecimalField(max_digits=9, decimal_places=2)

      def save(self):
            CacheControl(self.pk).delete_cache()
            CacheControl("list_home").delete_cache()
            return super().save()