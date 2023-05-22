from django.urls import path
from students.views import student_form, student_list

urlpatterns = [
    path('form/', student_form, name='student_form'),
    path('list/', student_list, name='student_list'),
]
