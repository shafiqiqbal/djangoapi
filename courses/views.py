from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets # some sets of pages that will be created for you
from .models import Course
from .serializers import CourseSerializer

class CourseView(viewsets.ModelViewSet):
	queryset = Course.objects.all() #pulling out your data from your database
	serializer_class = CourseSerializer #convert our database to/from json