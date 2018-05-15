from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from .models import School, Teacher, Student, Parent, Word
# Register your models here.

admin.site.register(School)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Word)
admin.site.site_header = 'More To Learn'

class SchoolSite(AdminSite):
    pass
    #or overwrite some methods for different functionality

class TeacherSite(AdminSite):
    pass

schooladmin = SchoolSite(name="schooladmin")
schooladmin.register(Teacher)
schooladmin.register(Student)
schooladmin.register(Parent)
schooladmin.register(Word)
schooladmin.site_header = 'More To Learn'

teacheradmin = TeacherSite(name="teacheradmin")
teacheradmin.register(Student)
teacheradmin.register(Parent)
teacheradmin.register(Word)
teacheradmin.site_header = 'More To Learn'