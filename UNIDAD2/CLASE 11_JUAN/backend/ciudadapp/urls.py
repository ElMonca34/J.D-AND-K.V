from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ciudadapp.views import ciudadViewSet

router = DefaultRouter()
router.register(r'ciudad', ciudadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]