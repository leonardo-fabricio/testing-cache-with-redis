from django.urls import path
from .views import *

urlpatterns = [
    path("api/listar_cache/", ListValuesCache),
    path("api/limpar_cache/", DeleteValuesCache),
    path("api/detalhe/<int:pk>/", DetailProduct.as_view()),
    path("api/listar_produtos", ListAllProducts.as_view()),
]
