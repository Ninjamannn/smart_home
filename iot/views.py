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
from iot.models import Bathroom, Liveroom
from iot.charts import chart_bathroom, chart_liveroom
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
    last_data = Bathroom.objects.last()
    return render(request, 'iot/climate.html', {'last_data': last_data})


@login_required(login_url='login')
def bathroom(request):
    last_data = Bathroom.objects.last()
    #today = datetime.date.today()
    #one_week = datetime.timedelta(weeks=1)
    #week = today - one_week
    #today_day = today.day
    #last_week = datetime.date.today().day - 7
    #datetime__range = [str(week), str(today)]
    cht = chart_bathroom(request, as_func=True)
    return render(request, 'iot/bathroom.html', {'Data': cht, 'last_data': last_data})


@login_required(login_url='login')
def liveroom(request):
    last_data = Liveroom.objects.last()
    #today = datetime.date.today()
    #one_week = datetime.timedelta(weeks=1)
    #week = today - one_week
    #today_day = today.day
    #last_week = datetime.date.today().day - 7
    #datetime__range = [str(week), str(today)]
    cht = chart_liveroom(request, as_func=True)
    return render(request, 'iot/liveroom.html', {'liveroomData': cht, 'last_data': last_data})



