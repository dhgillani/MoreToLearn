from rest_framework import serializers
from . import models


class WordSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		word = models.Word.objects.create(
		    word_text=validated_data['word_text'],
		    teacher = validated_data['teacher']
		)
		word.save()
		return word
	class Meta:
		fields = ('word_id', 'word_text','teacher')
		model = models.Word


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','username','name','first_name','last_name','email')
        model = models.Teacher


class StudentORParentSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		sop = models.StudentORParent.objects.create(
		    name=validated_data['name'],
		    username = validated_data['username'],
		    teacher = validated_data['teacher'],
		    standard = validated_data['standard'],
		    password = validated_data['password']
		)
		sop.save()
		return sop

	class Meta:
		fields = ('sp_id','name', 'standard','username','password','teacher')
		model = models.StudentORParent
		lookup_field = 'username'