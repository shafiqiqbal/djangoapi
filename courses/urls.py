from django.urls import path, include
from . import views

#routers allow you to create get and post request
#get request: you get something that is shown on the screen
#post request: post something to the database
#earlier you can add courses from admin area,
#by using this routers, it will create functionality to allow you to add somethig from the actual website itself.
from rest_framework import routers 

#creating variable:
router = routers.DefaultRouter()

#registering this router
#'courses' in this case is the url that you want to show
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
]