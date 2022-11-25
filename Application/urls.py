from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("api/listar_produtos/", ProductViewSet.as_view({'get': 'list'})),
    path("api/listar_cache/", ListValuesCache),
    path("api/limpar_cache/", DeleteValuesCache),
    path("api/detalhe/<int:pk>/", DetailProduct.as_view())
]
