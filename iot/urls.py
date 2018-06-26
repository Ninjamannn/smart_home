from django.conf.urls import url
from django.contrib.auth.views import logout
from django.urls import path
from . import views

from iot.models import Bathroom, Liveroom


urlpatterns = [
    path('', views.iot, name='iot'),
    path('login/', views.log_in, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('bathroom/api/climate/', views.climate, name='climate'),
    path('bathroom/api/chart/<int:period>', views.chart, {'model': Bathroom}, name='bathroom_chart'),
    path('liveroom/', views.liveroom, name='liveroom')
]
