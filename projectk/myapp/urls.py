from django.urls import path #Manam Create Cheskunna File
from . import views          #anni files lonchi views ni import chesko
                             #import views From All

urlpatterns = [
    
  path('',views.home,name='home') , 
  path('add',views.add,name='add')
    
]
