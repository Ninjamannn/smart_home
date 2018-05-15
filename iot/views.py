from chartit import DataPool, Chart
import time
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response
from django.urls import reverse
from django.views.generic import FormView
from django.contrib.auth import login as login_auth, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from django.shortcuts import render
from iot.models import Dht22


@login_required(login_url='login')
def iot(request):
    return render(request, 'iot/home.html')


@login_required(login_url='login')
def bathroom(request):
    # temp, hum = Dht22.get_data()
    return render(request, 'iot/bathroom.html')


def log_in(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active:
                login_auth(request, user)
                return HttpResponseRedirect(reverse(iot))
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'iot/login.html', context)


@login_required(login_url='login')
def climate(request):
    data = Dht22.objects.last()
    return render(request, 'iot/climate.html', {'data': data})


def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': Dht22.objects.all()},
              'terms': [
                'datetime',
                'temp_value',
                'hum_value']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'datetime': [
                    'temp_value',
                    'hum_value']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render(request, 'iot/charts.html', {'weatherchart': cht})
    #return render_to_response({'weatherchart': cht})
