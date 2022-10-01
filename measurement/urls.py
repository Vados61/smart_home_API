from django.urls import path

from measurement.views import SensorListView, SensorRetrieveView, MeasurementsView

urlpatterns = [
    path('sensors/', SensorListView.as_view()),
    path('sensors/<pk>/', SensorRetrieveView.as_view()),
    path('measurements/', MeasurementsView.as_view())
]
