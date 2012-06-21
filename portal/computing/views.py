# Create your views here.

from computing.models import Image, Details_OpenStack
from computing.models import ImageForm, Details_OpenStackForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from django.template import RequestContext
import djcelery
import tagging
import tagging.utils
import os

def index(request):
	latest_image_list = Image.objects.all().order_by('-name') [:5]
	return render_to_response('computing/index2.html', {'latest_image_list': latest_image_list})
def detail(request, image_id):
	i = get_object_or_404(Image, pk=image_id)
	return render_to_response('computing/image_detail.html', {'image': i})

def filetree(request):
	url = os.getcwd()
	dirList = os.listdir(url)
	latest_image_list = Image.objects.all().order_by('-name') [:5]
	return render_to_response('computing/detail.html', {'dirList': dirList, 'latest_image_list': latest_image_list})

def search_form(request):
	return render_to_response('computing/search_form.html')
	
def search(request):
    if 'q' in request.GET and request.GET['q']:
    	q = request.GET['q']
    	q = q.upper()
    	images = Image.objects.all()
    	l = list()
    	counter = 0
    	for image in images:
    		tags = image.get_tags()
    		for tag in tags:
    			if tag.name.upper() == q:
    				l.append((image.id, image.name))
#    				l.append(image.name)
    			

    	#l.append(tags)
    	#return HttpResponse(len(l))
    	#images = Image.objects.filter(name__icontains=q)
    	return render_to_response('computing/search_results.html', {'images': images, 'query': q, 'list': l})
    else:
    	return HttpResponse('Please submit a search term.')
