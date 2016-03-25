from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from reserve.models import Coach, ReserveTime, ReserveInterval, Student


# Create your views here.
def index(request):
    all_coach = Coach.objects.all()
    all_time = [one_time.reserve_time for one_time in ReserveTime.objects.all()]
    all_student = Student.objects.all()
    return render(request, 'index.html', locals())


def set_interval(request,minutes):
    ReserveInterval.objects.create(interval=int(minutes))
    return HttpResponseRedirect("/")  


def reserve(request):
    if request.method == 'POST':
        print "ss"
#         ReserveInterval.objects.create(interval=1)
    return HttpResponseRedirect("/") 
    