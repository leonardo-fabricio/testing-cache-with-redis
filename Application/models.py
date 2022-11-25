from django.db import models

from Application.utils import del_key

class ModelTestProduct(models.Model):
      name = models.CharField(max_length=255)
      description = models.TextField()
      price = models.DecimalField(max_digits=9, decimal_places=2)

      def save(self):
            del_key(self.pk)
            return super().save()