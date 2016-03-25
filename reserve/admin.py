from django.contrib import admin

from reserve.models import Coach, Student, Reserve, ReserveInterval, ReserveTime

class ReserveAdmin(admin.ModelAdmin):
    list_display = ('coach', 'starttime','endtime','student','reserve_date')
    
    
admin.site.register(Coach)
admin.site.register(Student)
admin.site.register(Reserve, ReserveAdmin)
admin.site.register(ReserveInterval)
admin.site.register(ReserveTime)