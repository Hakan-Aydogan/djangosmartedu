from django.urls import path
from .views import TeacherDetailView, TeacherListView


urlpatterns = [
    path('', TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>', TeacherDetailView.as_view(), name='teacher_detail'),
   
]