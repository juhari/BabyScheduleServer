from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('BabyScheduleUi.urls')),
    # url(r'^BabySchedule/', include('BabySchedule.foo.urls')),

    # url(r'^families/(?P<family_id>\d+)/$', 'BabyScheduleUi.views.family'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # rest frameworks browseable api
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
