from rest_framework.viewsets import ModelViewSet

from .models import Hamper
from .serializers import HamperSerializer


class HamperResource(ModelViewSet):
    queryset = Hamper.objects.all()
    serializer_class = HamperSerializer
