from rest_framework import generics

from .models import Word,Teacher,StudentORParent
from .serializers import WordSerializer,TeacherSerializer,StudentORParentSerializer
from django_filters.rest_framework import DjangoFilterBackend

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class WordDetail(generics.RetrieveAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

    # def get_queryset(self):
    # 	return Word.objects.all().filter(word_id=self.request.user)    


class TeacherList(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentORParentList(generics.ListCreateAPIView):
    queryset = StudentORParent.objects.all()
    serializer_class = StudentORParentSerializer


class StudentORParentDetail(generics.RetrieveAPIView):
    serializer_class = StudentORParentSerializer
    
    # username = self.kwargs['username']
    
    
    def get_object(self):
    	# queryset = StudentORParent.objects.all()
    	user = self.request.query_params.get('username', None)
    	obj = StudentORParent.objects.get(username=user)
    	self.check_object_permissions(self.request,obj)
    	return obj

	# def get_object(self):
	#     queryset = self.filter_queryset(self.get_queryset())
	#     # make sure to catch 404's below
	# 	obj = queryset.get(username=user,password=password)
	#     self.check_object_permissions(self.request, obj)
	#     return obj

    # def get_queryset(self):
    #     queryset = StudentORParent.objects.all()
    #     # username = self.kwargs['username']
    #     user = self.request.query_params.get('username', None)
    #     # password = self.request.query_params.get('password', None)
    #     if user is not None:
    #     	queryset = queryset.filter(username=user)
    #         # .filter(password=password)
    #     return queryset
