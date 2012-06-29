from django.shortcuts import render_to_response
from django.contrib.formtools.wizard import FormWizard

class StackWizard(FormWizard):
	def done(self, request, form_list):
		return render_to_response('done.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})
