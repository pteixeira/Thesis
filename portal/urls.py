from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings
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
    url(r'^computing/search/$', 'computing.views.search'),
    url(r'^computing/create_image/$', 'computing.views.create_image'),
    url(r'^computing/create_results/$', 'computing.views.create_results'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mymedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root':     settings.MEDIA_ROOT}),
)
