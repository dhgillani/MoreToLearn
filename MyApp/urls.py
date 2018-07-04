from django.urls import path,re_path

from . import views

urlpatterns = [
    path('words/', views.WordList.as_view()),
    path('words/<int:pk>/', views.WordDetail.as_view()),
    path('teachers/', views.TeacherList.as_view()),
    path('teachers/<int:pk>/', views.TeacherDetail.as_view()),
    path('sops/', views.StudentORParentList.as_view()),
    # path('sops/<int:pk>/', views.StudentORParentDetail.as_view()),
    re_path(r'^sops/(?P<username>.+)/$', views.StudentORParentDetail.as_view()),
    # path('sops/details/', views.StudentORParentDetail.as_view()),
]