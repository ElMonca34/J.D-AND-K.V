from rest_framework import viewsets
from .models import ciudad
from .serializers import ciudadSerializer

class ciudadViewSet(viewsets.ModelViewSet):
    queryset = ciudad.objects.all()
    serializer_class = ciudadSerializer
