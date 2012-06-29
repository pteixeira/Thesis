from computing.models import Image, Details_OpenNebula, Details_OpenStack, Image_Stack, Usage
from django.contrib import admin

class ImageAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,			{'fields': ['name']}),
#		('Date Information',	{'fields': ['date_added'], 'classes': ['collapse']}),
		('Detail Information',	{'fields': ['type_of_image', 'number_of_uses']})
	]
	list_display = ('name', 'number_of_uses')
#	list_display = ('name', 'date_added')
#	list_filter = ['date_added']
	search_fields = ['name']
	
admin.site.register(Image, ImageAdmin)
admin.site.register(Image_Stack)
admin.site.register(Usage)
