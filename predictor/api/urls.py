from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^devices/$', views.DeviceList.as_view(), name='devices-list'),
    url(r'^inputdata/$', views.InputDataList.as_view(), name='inputdata-list'),
]