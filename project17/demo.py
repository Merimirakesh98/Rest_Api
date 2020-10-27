import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'


def get_data(id=None):

	data = {}
	if id is not None:
		data  = {'id':id}

	response=requests.get(BASE_URL+END_POINT,data = json.dumps(data))
	print(response.status_code)
	print(response.json())





def post_data():
	sno=int(input('Enter the Student number:\t'))
	sname=input('Enter the Name of the student:\t')
	sphono=int(input('Enter the ph no of the student:\t'))
	saddress=input('Enter the Address of the student:\t')
	stud_data={'sno':sno,'sname':sname,'sphono':sphono,'saddress':saddress}

	response = requests.post(BASE_URL+END_POINT,data=json.dumps(stud_data))
	print(response.status_code)
	print(response.json())

if __name__ == '__main__':
	print('select the options below you want-->[get, post]')
	
	options=input('enter the options:\t')
	if options=='get':
		get_data()
	elif options=='post':
		post_data()



