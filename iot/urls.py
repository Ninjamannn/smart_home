from django.conf.urls import url
from django.contrib.auth.views import logout
from django.urls import path
from . import views
urlpatterns = [
    path('', views.iot, name='iot'),
    path('login/', views.log_in, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('bathroom/climate/', views.climate, name='climate'),
    path('charts/', views.weather_chart_view, name='charts'),
]
