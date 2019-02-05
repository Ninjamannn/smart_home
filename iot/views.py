from django.urls import reverse
from django.contrib.auth import login as login_auth, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from iot.models import Bathroom, Liveroom, BoilerRoom
from iot.charts import chart_bathroom, chart_liveroom, chart_boilerroom


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
def climate_bathroom(request):
    last_data = Bathroom.objects.last()
    return render(request, 'iot/climate.html', {'last_data': last_data})


@login_required(login_url='login')
def bathroom(request, **kwargs):
    if kwargs:
        cht = chart_bathroom(period=kwargs['period'])
        return render(request, 'iot/bathroom_chart.html', {'Data': cht})
    last_data = Bathroom.objects.last()
    cht = chart_bathroom(period=3)
    return render(request, 'iot/bathroom.html', {'Data': cht, 'last_data': last_data})


@login_required(login_url='login')
def climate_liveroom(request):
    last_data = dict(
        temp_value=Liveroom.objects.filter(type_value="temp").last().value,
        hum_value=Liveroom.objects.filter(type_value="hum").last().value,
        datetime=Liveroom.objects.last().datetime,
    )

    return render(request, 'iot/climate.html', {'last_data': last_data})


@login_required(login_url='login')
def liveroom(request, **kwargs):
    if kwargs:
        cht = chart_liveroom(period=kwargs['period'])
        return render(request, 'iot/liveroom_chart.html', {'Data': cht})
    last_data = Liveroom.objects.last()
    cht = chart_liveroom(period=3)

    return render(request, 'iot/liveroom.html', {'Data': cht, 'last_data': last_data})


@login_required(login_url='login')
def climate_boilerroom(request):
    last_data = dict(
        temp_value=BoilerRoom.objects.filter(type_value="temp").last().value,
        hum_value=0,
        datetime=BoilerRoom.objects.last().datetime,
    )

    return render(request, 'iot/climate_boilerroom.html', {'last_data': last_data})


@login_required(login_url='login')
def boilerroom(request, **kwargs):
    if kwargs:
        cht = chart_boilerroom(period=kwargs['period'])
        return render(request, 'iot/boilerroom_chart.html', {'Data': cht})
    last_data = BoilerRoom.objects.last()
    cht = chart_boilerroom(period=3)

    return render(request, 'iot/boilerroom.html', {'Data': cht, 'last_data': last_data})


def underconstruction(request):
    return render(request, 'iot/underconstruction.html')
