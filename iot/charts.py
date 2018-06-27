import datetime
from django.shortcuts import render
from chartit import DataPool, Chart

from iot.models import Bathroom, Liveroom


def chart_bathroom(as_func=False, default_period=3, **kwargs):
    model = Bathroom

    if as_func is True:
        period = default_period
    else:
        period = kwargs['period']
    day_ago = datetime.date.today().day - period

    if period == 1:
        chart_text = '24 hours'
    elif period == 7:
        chart_text = 'week'
    elif period == 30:
        chart_text = 'month'
    else:
        chart_text = str(period)+' days'

    #Step 1: Create a DataPool with the data we want to retrieve.
    modelData = \
        DataPool(
           series=
            [{'options': {
               'source': model.objects.filter(datetime__day__gte=day_ago)},
              'terms': [
                'datetime',
                'temp_value',
                'hum_value']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = modelData,
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
                   'text': 'Climate in my bathroom in the last ' + chart_text},
               'xAxis': {
                    'title': {
                       'text': 'Date/Time'}}})

    #Step 3: Send the chart object to the template.
    return cht


def chart_liveroom(as_func=False, default_period=3, **kwargs):
    model = Liveroom

    if as_func is True:
        period = default_period
    else:
        period = kwargs['period']
    day_ago = datetime.date.today().day - period

    if period == 1:
        chart_text = '24 hours'
    elif period == 7:
        chart_text = 'week'
    elif period == 30:
        chart_text = 'month'
    else:
        chart_text = str(period)+' days'

    #Step 1: Create a DataPool with the data we want to retrieve.
    modelData = \
        DataPool(
           series=
            [{'options': {
               'source': model.objects.filter(datetime__day__gte=day_ago)},
              'terms': [
                'datetime',
                'temp_value',
                'hum_value']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = modelData,
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
                   'text': 'Climate in my liveroom in the last ' + chart_text},
               'xAxis': {
                    'title': {
                       'text': 'Date/Time'}}})

    #Step 3: Send the chart object to the template.
    return cht
