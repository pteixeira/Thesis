from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http import HttpResponse
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portal.views.home', name='home'),
    # url(r'^portal/', include('portal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^computing/$', 'computing.views.index'),
#    url(r'^computing/$', 'computing.views.index2'),
    url(r'^computing/(?P<image_id>\d+)/$', 'computing.views.detail'),
    url(r'^computing/details', 'computing.views.filetree', name="list"),
    url(r'^computing/search_form/$', 'computing.views.search_form'),
    url(r'^search/$', 'computing.views.search'),
    url(r'^admin/', include(admin.site.urls)),
)
