from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):
  SCHOOL = 1
  TEACHER = 2
  ADMIN = 3
  ROLE_CHOICES = (
      (SCHOOL, 'school'),
      (TEACHER, 'teacher'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class User(AbstractUser):
  roles = models.ManyToManyField(Role)

class School(models.Model):
	school_id = models.AutoField(primary_key=True)
	school_name = models.CharField(max_length=300)
	password = models.CharField (max_length=50)

	def __str__(self):
		return self.school_name

	class Meta:
		ordering = ('school_id',)

class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=300)
	username = models.CharField (max_length=100)
	password = models.CharField (max_length=50)
 	# schools = models.ManyToManyField(School)
	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Student(models.Model):
	student_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=300)
	standard = models.CharField(max_length=50)
	username = models.CharField (max_length=100)
	password = models.CharField (max_length=50)
    # teachers = models.ManyToManyField(Teacher)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('name',)

class Parent(models.Model):
	parent_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=300)
	standard = models.CharField(max_length=50)
	username = models.CharField (max_length=100)
	password = models.CharField (max_length=50)

	def __str__(self):
		return self.name
	class Meta:
		ordering = ('name',)

class Word(models.Model):
	word_id = models.AutoField(primary_key=True) 
	word_text = models.CharField(max_length=300)

	def __str__(self):
		return self.word_text

	class Meta:
		ordering = ('word_text',)