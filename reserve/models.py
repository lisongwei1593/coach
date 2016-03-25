# -*- coding: utf-8 -*-s
from django.db import models
import datetime

class Coach(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'姓名')

    class Meta:
        verbose_name = verbose_name_plural = u'教练'

    def __unicode__(self):
            return self.name
        
    @property
    def reserve_time_list(self):
        available_list=[]
        available_time = ReserveTime.objects.all()
        all_reserve = self.reserve_coach.filter(reserve_date=datetime.datetime.today())
        for reserve in all_reserve:
            starttime = reserve.starttime.replace(hour=(reserve.starttime.hour-1))
            endtime = reserve.endtime
            available_time = available_time.exclude(reserve_time__gt=starttime,reserve_time__lt=endtime)
        for one_time in available_time:
            available_list.append(one_time.reserve_time)
        return available_list
        
                

class Student(models.Model):
    name = models.CharField(max_length=10, verbose_name=u'姓名')

    class Meta:
        verbose_name = verbose_name_plural = u'学员'

    def __unicode__(self):
            return self.name
        
        
class Reserve(models.Model):
    coach = models.ForeignKey(Coach, related_name='reserve_coach',verbose_name=u'教练')
    starttime = models.TimeField()
    endtime = models.TimeField()
    student = models.ForeignKey(Student, related_name='reserve_coach',verbose_name=u'学员')
    reserve_date = models.DateField()

    class Meta:
        verbose_name = verbose_name_plural = u'预约'
        
    
class ReserveInterval(models.Model):
    interval = models.IntegerField()
    
    class Meta:
        verbose_name = verbose_name_plural = u'预约间隔'
    
    def save(self, *args, **kwargs):
        ReserveInterval.objects.all().delete()
        ReserveTime.objects.all().delete()
        time_interval = datetime.timedelta(minutes=self.interval)
        starttime = datetime.datetime.strptime('08:00', '%H:%M')
        endtime = datetime.datetime.strptime('11:00', '%H:%M').time()
        ReserveTime.objects.create(reserve_time=starttime.time())
        while starttime.time() < endtime:
            starttime = starttime + time_interval
            ReserveTime.objects.create(reserve_time=starttime.time())
        super(ReserveInterval, self).save(*args, **kwargs)
    
    def __unicode__(self):
            return str(self.interval)
        
        
class ReserveTime(models.Model):
    reserve_time = models.TimeField()
    
    class Meta:
        verbose_name = verbose_name_plural = u'预约时间点'
        
    def __unicode__(self):
            return str(self.reserve_time)
