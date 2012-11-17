from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from BabyScheduleUi import views

urlpatterns = patterns('',
    url(r'^families/$', views.FamilyList.as_view()),
    url(r'^families/(?P<pk>[0-9]+)/$', views.FamilyDetail.as_view())
)

urlpatterns = format_suffix_patterns(urlpatterns)