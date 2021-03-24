from rest_framework import generics
from .models import Device, InputData
from .serializers import DeviceSerializer, InputDataSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class InputDataList(generics.ListCreateAPIView):
    queryset = InputData.objects.all()
    serializer_class = InputDataSerializer
