from django import forms

from testapp.models import Student

class StudentForm(forms.ModelForm):
	def clean_sno(self):
		input_sno = self.cleaned_data['sno']
		if input_sno<9:
			raise forms.ValidationError('The minimum student number  should be more than 9')
		return input_sno


	class Meta:
		model=Student
		fields='__all__'