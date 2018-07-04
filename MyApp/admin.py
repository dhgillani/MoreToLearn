from django.contrib.admin.sites import AdminSite
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from MyApp.models import Teacher as MyUser
from .models import  Teacher, StudentORParent, Word
from django import forms
from django.contrib.auth.models import Group



class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = MyUser


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            MyUser.objects.get(username=username)
        except MyUser.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class MyUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )


# # Register your models here.

# admin.site.register(School)
admin.site.register(StudentORParent)
admin.site.register(Word)
admin.site.site_header = 'More To Learn'
admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)


# class TeacherSite(AdminSite):
#     pass

# teacheradmin = TeacherSite(name="teacheradmin")
# teacheradmin.register(StudentORParent)
# teacheradmin.register(Word)
# teacheradmin.site_header = 'More To Learn'





