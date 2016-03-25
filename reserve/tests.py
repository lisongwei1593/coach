import django
import datetime

from django.test import TestCase

from reserve.models import ReserveTime, Coach
django.setup()


cco = Coach.objects.get(id=1)
list = cco.reserve_time_list
print list
ss= [one_time.reserve_time for one_time in ReserveTime.objects.all()]
print ss