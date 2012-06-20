from django.db import models
import time
from tagging.fields import TagField
from tagging.models import Tag
import tagging.models
from django.forms import ModelForm
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

class Image(models.Model):
	name = models.CharField(max_length=500)
	date_added = models.DateTimeField('date added to system')
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

class ImageForm(ModelForm):
	class Meta:
		model = Image
		
class Details_OpenStack(models.Model):
	image = models.ForeignKey(Image)
	kernel_id = models.CharField(max_length=500) #can be kernel-id
	size = models.IntegerField()
	public = models.BooleanField()
	date_updated = models.DateTimeField('date updated')
	image_status = models.CharField(max_length=100)
#	kernel_id = image_id*
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

