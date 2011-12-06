# Create your views here.

from computing.models import Image
from django.shortcuts import render_to_response, get_object_or_404
import os

def index(request):
	latest_image_list = Image.objects.all().order_by('-date_added') [:5]
	return render_to_response('computing/index.html', {'latest_image_list': latest_image_list})
def detail(request, image_id):
	i = get_object_or_404(Image, pk=image_id)
	return render_to_response('computing/detail.html', {'image': i})

def filetree(request):
	url = os.getcwd()
	return render_to_response('computing/directory.html', {'url': url})
