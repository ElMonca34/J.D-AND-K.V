from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CuidadViewSet

routers = DefaultRouter()
routers.register(r'ciudad', CuidadViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]

