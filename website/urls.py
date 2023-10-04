from django.urls import path
from . import views #the period means from inside this directory (website)

urlpatterns = [
    
    path('', views.home, name="home"), #the path '' means root path, views references views.py file
    path('home.html', views.contact, name="contact"), #the path 'not empty' means path to specific file, views references views.py file

] 
