from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarroViewSet

routers = DefaultRouter()
routers.register(r'carro', CarroViewSet)

urlpatterns = [
 path('', include(routers.urls)),
]