from django.shortcuts import render
from django.views.generic import View
from testapp.models import Student
from django.http import HttpResponse
import json
from django.core.serializers import serialize
from testapp.mixins import *

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from testapp.utils import is_data_json
from testapp.forms import StudentForm

@method_decorator(csrf_exempt,name='dispatch')
class StudentCompleteCRUDusingCbv(MixinHttpResponse,SerializeMixin,View):
	def get_object_data_by_id(self, id):
		try:
			stud = Student.objects.get(id = id)
		except Student.DoesNotExist:
			stud = None
		return stud

	def get(self,request,*args,**kwargs):
		data = request.body
		#checking whether the data is Json or not
		valid_json_data = is_data_json(data)

		if not valid_json_data:
			json_data = json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		#converting Json data into Dictionary
		provided_data = json.loads(data)

		id = provided_data.get('id',None)
		if id is not None:
			stud= self.get_object_data_by_id(id)
			if stud is None:
				json_data = json.dumps({'msg':'The required source is not available'})
				return self.render_to_http_response(json_data,status=404)
			json_data = self.serialize([stud,])
			return self.render_to_http_response(json_data)

		#if the id is None
		query_string = Student.objects.all()
		json_data = self.serialize(query_string)
		return self.render_to_http_response(json_data)

	def post(self,request,*args,**kwargs):
		data=request.body
		valid_json_data=is_data_json(data)
		if not valid_json_data:
			json_data=json.dumps({'msg':'Please send the valid json data'})
			return self.render_to_http_response(json_data,status=400)

		stud_data = json.loads(data)

		form = StudentForm(stud_data)
		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg':'Resource created successfully'})
			return self.render_to_http_response(json_data)

		if form.errors:
			json_data=json.dumps(form.errors)
			return self.render_to_http_response(json_data,status=400)

	




	



