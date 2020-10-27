from django.contrib import admin

from testapp.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    '''
        Admin View for Student
    '''
    list_display = ('sno','sname','sphono','saddress')
    

admin.site.register(Student, StudentAdmin)