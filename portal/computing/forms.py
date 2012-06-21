from django.shortcuts import render_to_response
from django.contrib.formtools.wizard import FormWizard
from subprocess import call
import subprocess

class StackWizard(FormWizard):
	def get_template(self, step):
		return 'computing/create_stack_wizard.html'
	def done(self, request, form_list):
		subprocess.call(["/home/pedro/Desktop/scripts/test.sh"])
		return render_to_response('computing/done.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})
