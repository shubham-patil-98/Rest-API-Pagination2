from django.http import HttpResponse
from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .mypagination import MyPageNumberPagination
from django.http import HttpResponse

# Create your views here.
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPageNumberPagination

def home(request):
    return HttpResponse("add /studentapi behind 8000")