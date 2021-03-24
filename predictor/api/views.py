from rest_framework import generics
from .models import Device, InputData
from .serializers import DeviceSerializer, InputDataSerializer

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class InputDataList(generics.ListCreateAPIView):
    serializer_class = InputDataSerializer
    def get_queryset(self):
        queryset = InputData.objects.all()
        device = self.request.query_params.get('device', None)
        if device is not None:
            queryset = queryset.filter(device=device)
        return queryset