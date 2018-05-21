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
from iot.models import Dht22Bathroom
import datetime


@login_required(login_url='login')
def iot(request):
    return render(request, 'iot/home.html')


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
    last_data = Dht22Bathroom.objects.last()
    return render(request, 'iot/climate.html', {'last_data': last_data})


@login_required(login_url='login')
def bathroom(request):
    last_data = Dht22Bathroom.objects.last()
    #today = datetime.date.today()
    #one_week = datetime.timedelta(weeks=1)
    #week = today - one_week
    #today_day = today.day
    #last_week = datetime.date.today().day - 7
    #datetime__range = [str(week), str(today)]
    cht = chart(request, as_func=True, period=3)
    return render(request, 'iot/bathroom.html', {'dht22BathroomData': cht, 'last_data': last_data})


def chart(request, as_func=False, period=7):       # TODO сделать универсальную функцию для каждого помещения
    period_day = datetime.date.today().day - period
    #Step 1: Create a DataPool with the data we want to retrieve.
    dht22BathroomData = \
        DataPool(
           series=
            [{'options': {
               'source': Dht22Bathroom.objects.filter(datetime__day__gte=period_day)},
              'terms': [
                'datetime',
                'temp_value',
                'hum_value']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = dht22BathroomData,
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
                   'text': 'Climate in my bathroom'},
               'xAxis': {
                    'title': {
                       'text': 'Date/Time'}}})

    #Step 3: Send the chart object to the template.
    if as_func is True:
        return cht
    else:
        return render(request, 'iot/bathroom_chart.html', {'dht22BathroomData': cht})
