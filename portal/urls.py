from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings
from computing.forms import StackWizard
from computing.models import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
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
    url(r'^computing/login/', 'django.contrib.auth.views.login'),
    url(r'^computing/logout/$', 'computing.views.logout_page'),
    url(r'^computing/management/$', 'computing.views.management'),
    url(r'^computing/user/(?P<user_id>\d+)/$', 'computing.views.user_details'),
    url(r'^computing/modify_user/(?P<user_id>\d+)/$', 'computing.views.modify_user'),
    url(r'^computing/modify_user_results', 'computing.views.modify_user_results'),
    url(r'^computing/list_vms', 'computing.views.list_vms'),    
    url(r'^computing/show_tasks/$', 'computing.views.show_tasks'),
    url(r'^computing/update_tasks/$', 'computing.views.update_tasks'),
#    url(r'^computing/$', 'computing.views.index2'),
    url(r'^computing/(?P<image_id>\d+)/$', 'computing.views.detail'),
    url(r'^computing/details', 'computing.views.filetree', name="list"),
    url(r'^computing/search_form/$', 'computing.views.search_form'),
    url(r'^computing/search/$', 'computing.views.search'),
    url(r'^computing/create_image/$', 'computing.views.create_image'),
    url(r'^computing/create_results', 'computing.views.create_results'),
    url(r'^computing/create_negocio/$', StackWizard([Image_StackForm, Details_StackForm])),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mymedia/(?P<path>.*)$', 'django.views.static.serve', {'document_root':     settings.MEDIA_ROOT}),
)


urlpatterns += staticfiles_urlpatterns()
