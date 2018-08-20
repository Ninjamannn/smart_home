import datetime
from chartit import DataPool, Chart

from iot.models import Bathroom, Liveroom


def chart_bathroom(**kwargs):
    model = Bathroom

    period = kwargs['period']
    date_range = datetime.date.today() - datetime.timedelta(period)

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
               'source': model.objects.filter(datetime__gte=date_range)},
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
                   'text': 'Climate in my bathroom for the last ' + chart_text},
               'xAxis': {
                    'title': {
                       'text': 'Date/Time'}}})

    #Step 3: Send the chart object to the template.
    return cht


def chart_liveroom(**kwargs):
    model = Liveroom

    period = kwargs['period']
    date_range = datetime.date.today() - datetime.timedelta(period)

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
               'source': model.objects.filter(datetime__gte=date_range)},
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
                   'text': 'Climate in my living room for the last ' + chart_text},
               'xAxis': {
                    'title': {
                       'text': 'Date/Time'}}})

    #Step 3: Send the chart object to the template.
    return cht
