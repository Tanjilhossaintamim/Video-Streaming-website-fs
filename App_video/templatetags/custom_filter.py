from django import template
from datetime import datetime
from django.utils.timezone import now,make_aware
from django.utils.timesince import timesince


register = template.Library()

def filter(value):
    if len(value)<35:
        return value
    return value[0:35]+'...'
register.filter('filter',filter)

def calulate_time(time):
    current_date=now()
    
    return timesince(time,current_date)
register.filter('calulate_time',calulate_time)


