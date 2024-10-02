from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('flood/report', views.report, name='flood_report'),
  path('alert/1', views.alert1, name='alert1'),
  path('alert/2', views.alert2, name='alert2'),
  path('alert/3', views.alert3, name='alert3'),
]