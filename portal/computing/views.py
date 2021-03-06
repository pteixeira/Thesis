# Create your views here.

from computing.models import Image, Details_OpenStack, Tag_Search_Frequency, Usage, User_Tasks, UserForm
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from django.template import RequestContext
from computing.models import Image_Stack, Image_StackForm
import tagging
import tagging.utils
from tagging.models import Tag, TaggedItem
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import models
from datetime import datetime, date
import datetime
import tasks
from celery.task import Task
#from computing.models import User_details
	
	
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/computing') #returns to the start page

@login_required
def management(request):
	image_list = Image_Stack.objects.all()
	user_in_session = request.user
	user_images = Image_Stack.objects.all()
	deletion_images = Image_Stack.objects.filter(status='delete')
#	user_images2 = list()
#	for image in user_images:
#		user_images2.append(image.get_time_in_system().days)
	
	return render_to_response('computing/management.html', {'image_list': image_list, 'user_in_session': user_in_session, 
								'user_images': user_images, 'images_deleted': deletion_images})

@login_required
def user_details(request, user_id):
	user_in_session = request.user
	user_image_list = Image_Stack.objects.filter(user_owner = request.user) #list of the user created images
	return render_to_response('computing/user_details.html', {'user_in_session': user_in_session, 'user_image_list': user_image_list})

@login_required
def modify_user(request, user_id):
	form = UserForm()
	return render_to_response('computing/modify_user.html', {'form': form}, context_instance=RequestContext(request))

@login_required	
def modify_user_results(request):
	if request.POST['first_name']:
		user = User.objects.get(id=request.user.id)
		user.name = request.POST['first_name']
		user.save()
	#user = request.POST['first_name']
	return render_to_response('computing/modify_user_results.html', {'user': user})

@login_required
def list_vms(request):
	public_image_list = Image_Stack.objects.filter(public = True) #list of the public images
	user_image_list = Image_Stack.objects.filter(user_owner = request.user) #list of the user created images
	#lists of public and user created images
	user_image_listlist = list(user_image_list)
	public_image_listlist = list(public_image_list)
	
	for item in user_image_listlist:
		for item2 in public_image_listlist:
			if item == item2:
				public_image_listlist.remove(item2)			
	
	user_image_listlist.extend(public_image_listlist)
	return render_to_response('computing/list_vms.html', {'user_image_list': user_image_listlist, 'user_in_session': request.user})


@login_required
def index(request):
	if not request.user.is_authenticated():
		return render_to_response('computing/login_error.html')
	else:
		user_in_session = request.user
		
		latest_image_list = Image_Stack.objects.all().order_by('-name') 
		c = RequestContext(request)
		return render_to_response('computing/index2.html', {'latest_image_list': latest_image_list, 'user_in_session': user_in_session}, c)
@login_required
def detail(request, image_id):
	user_in_session = request.user
	i = get_object_or_404(Image_Stack, pk=image_id)
	return render_to_response('computing/image_detail.html', {'image': i, 'user': user_in_session})

@login_required	
def create_image(request):
	imageForm = Image_StackForm()
	return render_to_response('computing/create_image.html', {'formset': imageForm, 'user_in_session': request.user}, context_instance=RequestContext(request))

@login_required
def create_results(request):
	if not request.POST['name']:
		return render_to_response('computing/create_results_error.html', {'no_name': 'dummy', 'user_in_session': request.user})
	post_data = request.POST.lists()
	dummy = 1
	if Image_Stack.objects.filter(name=request.POST['name'].upper()): #check if image already exists
		return render_to_response('computing/create_results_error.html', {'error': request.POST['name'], 'user_in_session': request.user})
	else:
		dummy = 1
	user1 = request.user #get user that is currently creating the image

	packages = "#!/bin/bash \nsudo vmbuilder kvm ubuntu --suite=precise --flavour=virtual --arch=i386 --mirror=http://de.archive.ubuntu.com/ubuntu -o --libvirt=qemu:///system --ip=192.168.0.101 --gw=192.168.0.1 --part=vmbuilder.partition --templates=mytemplates --user=user --name=Administrator --pass=password --firstboot=/home/pedro/Desktop/scripts/boot.sh --mem=256 --addpkg=vim-nox --addpkg=unattended-upgrades --addpkg=acpid "
	for x in range(0, len(post_data)):
		if post_data[x][0] == "matlab":
			packages = packages+"--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "vim":
			packages = packages+"--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "abaqus":
			packages = "--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "gcc":
			packages = "--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "openfoam":
			packages = "--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "gromacs":
			packages = "--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "ansys":
			packages = "--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "r":
			packages = "--addpkg="+post_data[x][0]+" \ "
		elif post_data[x][0] == "name":
			packages = packages+"--hostname="+request.POST['name']+" \ "
#	
	#script generation

	f = open('/home/pedro/Desktop/scripts/derp.sh', "r+")
	f.write(packages)
	f.close()
	
	derp = tasks.add.delay()
	derp = derp.task_id
	User_Tasks(user=request.user, task=derp).save()
	

	
	return render_to_response('computing/create_results.html', {'data': packages, 'user_in_session': request.user})
#	if i:
#		return render_to_response('computing/image_exists.html', {'data': post_data[0][1][0]})
#	else:	
#		#create the image
#		i = Image_Stack.objects.all().create(name=post_data[0][1][0].upper(), size=12,
#			 				     tags=post_data[1][1][0], kernel_id=post_data[2][1][0], 
#			 				     container_format=post_data[3][1][0], number_of_uses=10,
#			 				     ramdisk_id=post_data[4][1][0], disk_format=post_data[5][1][0], 
#							     type_of_image=post_data[6][1][0], image_status=post_data[7][1][0], 
#							     architecture=post_data[8][1][0], user_owner=user1)
#		i.save()
#		return render_to_response('computing/create_results.html', {'data': i})	

@login_required # shows user tasks
def show_tasks(request):
	tasks = User_Tasks.objects.filter(user=request.user)
	task_list = list()
	for i in tasks:
		result = Task.AsyncResult(i.task)
		task_list.append(result)
		
	return render_to_response('computing/show_tasks.html', {'tasks': task_list})


def update_tasks(request):
	#no POST vai receber as tasks que nao estao completas
	post_list = request.POST['id_list'] #vem do ajax lista de ids de tasks incompletas
	completed_tasks = list()
	f = open('/home/pedro/Desktop/aoisdnb.txt', 'w')
	f.write('derp')
	f.close()
	for li in post_list:
		if Task.AsyncResult(li).ready():#se task estiver completa
			completed_tasks.append(li)
	return HttpResponse(str(completed_tasks))

@login_required
def filetree(request):

	#initializing variables
	latest_image_list = list()
	public_image_list = Image_Stack.objects.filter(public = True) #list of the public images
	user_image_list = Image_Stack.objects.filter(user_owner = request.user) #list of the user created images
	most_searched_tags = Tag_Search_Frequency.objects.all().order_by('-freq')
	
	#--- user in session so it shows only his images	
	user_in_session = request.user
	
	#user's most used images
	user_most_used_images = Usage.objects.filter(user=user_in_session).order_by('-number_of_uses') [:5]
	
	#--- end of user's most used images
	
	#lists of public and user created images
	user_image_listlist = list(user_image_list)
	public_image_listlist = list(public_image_list)
	
	for item in user_image_listlist:
		for item2 in public_image_listlist:
			if item == item2:
				public_image_listlist.remove(item2)			
	
	user_image_listlist.extend(public_image_listlist)
	
	#--- end of lists of public and user created images					
#	latest_image_list.append(user_image_list)
#	latest_image_list.append(public_image_list)
#	user_list = User.objects.all()	
	

	
	#--- list of all the images
	full_image_list = Image_Stack.objects.all()
	
	#--- list ordered by number of uses across the system
	ordered_by_usage = Image_Stack.objects.all().order_by('-number_of_uses') [:5]
	return render_to_response('computing/detail.html', {'ordered_by_usage': ordered_by_usage, 'latest_image_list': user_image_listlist,
				  			    'user': user_in_session, 'full_image_list': full_image_list,
				  			    'user_most_used_images': user_most_used_images,
				  			    'most_searched_tags': most_searched_tags, 'user_in_session': request.user})

@login_required
def search_form(request):
	return render_to_response('computing/search_form.html', {'user_in_session': request.user})

@login_required	
def search(request):#se for so uma tag, devolve as imagens com essa tag 
    if 'q' in request.GET and request.GET['q']:
    	q = request.GET['q']
    	q = q.split(', ')
    	query = request.GET['q']
    	
    	#criar lista de frequencias de tags pesquisadas
    	for item in q:
    		if Tag_Search_Frequency.objects.filter(tag=item):
    			tag_found = Tag_Search_Frequency.objects.get(tag=item)
    			tag_found.freq = tag_found.freq + 1
    			tag_found.save()
    		else:
    			tag_found = Tag_Search_Frequency.objects.all().create(tag=item, freq = 1)
    			tag_found.save()
    	
    	#metodo de pesquisa
    	taggy2 = list()
    	list_of_images = list()
    	listinha = list()
    	dummy = 0
    	

    	for item in q:
    		try:
    			taggy = Tag.objects.get(name=item)
    		except Tag.DoesNotExist: 
    			return render_to_response('computing/search_results.html')
    		cenassas = TaggedItem.objects.get_by_model(models.Image_Stack, taggy)
		for i in cenassas:
			if i in listinha:
				dummy = 1
    			else:
				listinha.append(i)

	#coiso = TaggedItem.objects.get_by_model(models.Image_Stack, taggy2)
	#tag_list = Tag_Search_Frequency.objects.get(tag = tag_found.tag).freq
	
	return render_to_response('computing/search_results.html', {'image_list': listinha, 'searched_item': query, 
							            'user_in_session': request.user})
#	
#    	q = q.upper()
#    	images = Image_Stack.objects.all()
#    	l = list()
#    	counter = 0
#    	for image in images:
#    		tags = image.get_tags()
#    		for tag in tags:
#    			if tag.name.upper() == q:
#    				l.append((image.id, image.name))
    	#return render_to_response('computing/search_results.html', {'images': images, 'query': q, 'list': l}) --> this works!
    else:
    	return render_to_response('computing/search_results.html', {'user_in_session': request.user})
