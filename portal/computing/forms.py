from django.shortcuts import render_to_response
from django.contrib.formtools.wizard import FormWizard
from subprocess import call
import subprocess
import tasks
from computing.models import Image, Details_OpenStack

class StackWizard(FormWizard):
	def get_template(self, step):
		return 'computing/create_stack_wizard.html'
	def done(self, request, form_list):
		images = Image.objects.all()
		form_data = [form.cleaned_data for form in form_list]
		i = Image.objects.create(name = form_data[0]['name'],
					 type_of_image = form_data[0]['type_of_image'],
					 tags = form_data[0]['tags'],
					 number_of_uses = form_data[0]['number_of_uses'])
		#d = 
		
#		form_list[0]['number_of_uses'] #first form - 12
#		form_list[1] #second form
		#tasks.add.delay()
		#subprocess.call(["/home/pedro/Desktop/scripts/test.sh"]) 
		return render_to_response('computing/done.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})
