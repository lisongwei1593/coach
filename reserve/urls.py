# encoding: utf-8


from django.conf.urls import patterns, url

urlpatterns = patterns('reserve.views',
    url(r'^$', 'index', name='index'),
    url(r'^set_interval/(?P<minutes>\d+)/$', 'set_interval', name='set_interval'),
    url(r'^reserve/$', 'reserve', name='reserve'),
)
