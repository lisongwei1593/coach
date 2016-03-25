# -*- coding: utf-8 -*-s
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
import datetime,traceback
from reserve.models import Coach, ReserveTime, ReserveInterval, Student, Reserve


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
        try:
            coach_id = request.POST.get("coach_id")
            coach = Coach.objects.get(id=coach_id)
            time_str = request.POST.get('time')
            reserve_time = datetime.datetime.strptime(time_str, '%H:%M')
            endtime = reserve_time + datetime.timedelta(hours=1)
            #省略了登陆注册，此处默认为学员A
            student = Student.objects.get(id=1)
            Reserve.objects.create(coach=coach,starttime=reserve_time.time(),
                                   endtime=endtime.time(),student=student,reserve_date=datetime.datetime.today())
            return HttpResponse("ok")
        except:
            traceback.print_exc()
            return HttpResponse(u"预约失败")

