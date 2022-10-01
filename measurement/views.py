from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorListSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorListView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorRetrieveView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        data = request.data
        sensor = Sensor.objects.get(id=data['sensor'])
        temperature = data['temperature']
        Measurement(sensor=sensor, temperature=temperature).save()
        return Response({'status': 'OK'})



