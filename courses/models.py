from django.db import models

class Course(models.Model): #create class of the module
	name = models.CharField(max_length=200) #define the things that you want to save. Can google on django/sql data type
	language = models.CharField(max_length=100)
	price = models.CharField(max_length=10)

	def __str__(self): #self is your class
		return self.name



