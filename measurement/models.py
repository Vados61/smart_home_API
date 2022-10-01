from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()


class Measurement(models.Model):
    temperature = models.DecimalField(max_digits=100, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
