from django.db import models
from django.contrib.auth.models import AbstractUser

class Teacher(AbstractUser):
	name = models.CharField(max_length=100, blank=None)
	class Meta:
		ordering = ('name',)

class StudentORParent(models.Model):
	sp_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=300,blank=None)
	standard = models.CharField(max_length=50,blank=True)
	username = models.CharField(max_length=300,blank=None,unique=True)
	password = models.CharField(max_length=50,blank=None)
	teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True,blank=True) 
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Word(models.Model):
	word_id = models.AutoField(primary_key=True) 
	word_text = models.CharField(max_length=300,blank=None)
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
	def __str__(self):
		return self.word_text

	class Meta:
		ordering = ('word_text',)