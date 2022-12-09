from rest_framework import serializers
from .models import ModelTestProduct

class ModelTestProductSerializer(serializers.ModelSerializer):
      class Meta:
            model = ModelTestProduct
            fields = ('__all__')