from rest_framework import serializers
from .models import Device, InputData

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class InputDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputData
        fields = ['value','type','status', 'datetime', 'device']