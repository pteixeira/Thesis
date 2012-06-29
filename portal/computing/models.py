from django.db import models
import time
from tagging.fields import TagField
from tagging.models import Tag
import tagging.models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from datetime import date
from datetime import datetime
import datetime
# Create your models here.


IMAGE_CHOICES = (
	('stack', 'OpenStack Image'),
	('nebula', 'OpenNebula Image'),
)

	
TYPE_CHOICES = (
	('OS', 'Operating System Image'),
	('CDROM', 'CDROM Image'),
	('DATABLOCK', 'Datablock Image'),
)

BUS_CHOICES = (
	('IDE', 'IDE Bus'),
	('SCSI', 'SCSI Bus'),
	('virtio', 'virtio KVM Bus'),
)

DRIVER_CHOICES = (
	('raw', 'KVM RAW'),
	('qcow2', 'KVM QCOW2'),
	('tap', 'XEN TAP'),
	('aio', 'XEN AIO'),
	('file', 'file: '),
)

class Tag_Search_Frequency(models.Model):
	freq = models.IntegerField(null=True)
	tag = models.CharField(max_length=20, null = True)
	


class Image(models.Model):
	name = models.CharField(max_length=500)
#	date_added = models.DateTimeField('date added to system')
	type_of_image = models.CharField(max_length=10, choices=IMAGE_CHOICES) #can be OpenStack or OpenNebula - Different Details
	number_of_uses = models.IntegerField(blank=True, null=True)
	tags = tagging.fields.TagField()
	
	def set_tags(self, tags):
		Tag.objects.update_tags(self, tags)
	def get_tags(self):
		return Tag.objects.get_for_object(self)
		
	def __unicode__(self):
		return self.name
	
	def when_added(self):
		return self.date_added.date()

#class ImageForm(ModelForm):
#	class Meta:
#		model = Image

class Image_Stack(models.Model):
	name = models.CharField(max_length=500)
	user_owner = models.ForeignKey(User)
	date_added = models.DateField('date added to system', null = True)
	date_last_used = models.DateField(null = True)
	type_of_image = models.CharField(max_length=10, choices=IMAGE_CHOICES) #can be OpenStack or OpenNebula - Different Details
	number_of_uses = models.IntegerField(blank=True, null=True)
	tags = tagging.fields.TagField()
	kernel_id = models.CharField(max_length=500, null = True) #can be kernel-id
	size = models.IntegerField(null=True)
	public = models.BooleanField()
	image_status = models.CharField(max_length=100, null = True)
	ramdisk_id = models.CharField(max_length=200, blank=True, null=True)
	architecture = models.CharField(max_length=200, blank=True, null=True)
	container_format = models.CharField(max_length=200, blank=True, null=True)
	disk_format = models.CharField(max_length=200, blank=True, null=True)
	vim = models.BooleanField()
	matlab = models.BooleanField()
	abaqus = models.BooleanField()
	gcc = models.BooleanField()
	r = models.BooleanField()
	octave = models.BooleanField()
	gromacs = models.BooleanField()
	openfoam = models.BooleanField()
	ansys = models.BooleanField()
	#tag = TagField()
	
	
	def set_tags(self, tags):
		Tag.objects.update_tags(self, tags)
	def get_tags(self):
		return Tag.objects.get_for_object(self)
	def get_time_in_system(self):
		return self.date_added - datetime.date.today()
	def get_time_since_last_used(self):
		return self.date_last_used - datetime.date.today()
	
	
	def __unicode__(self):
		return self.name

class Usage(models.Model):
	user = models.ForeignKey(User)
	image = models.ForeignKey(Image_Stack)
	number_of_uses = models.IntegerField(null=True)
	
class User_Tasks(models.Model):
	user = models.ForeignKey(User)
	task = models.TextField(null=True)


class Image_StackForm(ModelForm):
	class Meta:
		model = Image_Stack
		exclude = ('number_of_uses', 'size', 'user_owner')

class Details_OpenStack(models.Model):
	image = models.ForeignKey(Image)
	kernel_id = models.CharField(blank=True,max_length=500) #can be kernel-id
	size = models.IntegerField(blank=True, null=True)
	public = models.BooleanField()
	image_status = models.CharField(max_length=100)
	ramdisk_id = models.CharField(max_length=200, blank=True, null=True)
	architecture = models.CharField(max_length=200, blank=True, null=True)
	container_format = models.CharField(max_length=200, blank=True, null=True)
	disk_format = models.CharField(max_length=200, blank=True, null=True)

class Details_OpenNebula(models.Model):
	image = models.ForeignKey(Image)
	image_name = models.CharField(max_length=500, unique=True)
	description = models.CharField(max_length=500)
	image_type = models.CharField(max_length=10, choices =TYPE_CHOICES)
	public = models.BooleanField(default=False)
	persistent = models.BooleanField(default=False)
	dev_prefix =  models.CharField(max_length=10, default='hd')
	bus = models.CharField(max_length=10, choices=BUS_CHOICES)
	driver = models.CharField(max_length=10, choices=DRIVER_CHOICES)
	path = models.CharField(max_length=100, blank=True, null=True) #mandatory if no SOURCE
	source = models.CharField(max_length=200, blank=True, null=True) #mandatory if no PATH
	#mandatory for DATABLOCK images w/o PATH:
	size = models.IntegerField()
	fstype = models.CharField(max_length=50)
	def __unicode__(self):
		return self.image_name


class Details_StackForm(forms.Form):
	image = models.ForeignKey(Image)
	kernel_id = forms.CharField(max_length=500)
	size = forms.IntegerField()
	public = forms.BooleanField()
#	date_updated = forms.CharField()
	image_status = forms.CharField(max_length=100)
	ramdisk_id = forms.CharField(max_length=200)
	architecture = forms.CharField(max_length=200)
	container_format = forms.CharField(max_length=200)
	disk_format = forms.CharField(max_length=200)

#class Image_StackForm(forms.Form):
#	name = forms.CharField(max_length=500)
##	date_added = forms.DateTimeField(default=datetime.date.today)
#	type_of_image = forms.ChoiceField(choices=IMAGE_CHOICES) #can be OpenStack or OpenNebula - Different Details
#	number_of_uses = forms.CharField(max_length=2)
#	tags = forms.CharField(max_length=30)

#class Details_OpenStackForm(ModelForm):
#	class Meta:
#		model = Details_OpenStack
#		#exclude = ('image',)

#class User_details(models.Model):
#	user = models.OneToOneField(User)

