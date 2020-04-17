#This is our serializers
from rest_framework import serializers
from .models import Course

#create new class
class CourseSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Course 
		fields = ('id', 'url', 'name', 'language', 'price')
