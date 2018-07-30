from django.conf.urls import url
from django.contrib.auth.views import logout
from django.urls import path
from . import views


urlpatterns = [
    path('', views.iot, name='iot'),
    path('login/', views.log_in, name='login'),
    path('logout/', logout, {'next_page': 'login'}, name='logout'),

    path('bathroom/', views.bathroom, name='bathroom'),
    path('bathroom/api/climate/', views.climate_bathroom, name='bathroom_climate'),
    path('bathroom/api/chart/<int:period>', views.bathroom, name='bathroom_chart'),

    path('liveroom/', views.liveroom, name='liveroom'),
    path('liveroom/api/climate/', views.climate_liveroom, name='liveroom_climate'),
    path('liveroom/api/chart/<int:period>', views.liveroom, name='liveroom_chart'),

    path('underconstruction/', views.underconstruction, name='underconstruction'),
]
