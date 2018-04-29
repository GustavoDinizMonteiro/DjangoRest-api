from rest_framework.serializers import ModelSerializer

from .models import Hamper


class HamperSerializer(ModelSerializer):
    class Meta:
        model = Hamper
        fields = '__all__'
