from django.urls import path #import path from project urls.py
from . import views #import views from all 

urlpatterns =[
    path('',views.index, name='index')
  
]
#mutiple urls to mapping will be withing this array
#IN views.home home means there will be a home function