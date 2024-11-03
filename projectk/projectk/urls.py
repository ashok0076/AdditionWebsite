"""
URL configuration for projectk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include #include Function ni import Cheskunnam..

urlpatterns = [
    path('',include('myapp.urls')), #Edi Main urls file kada so 
    #project urls ni kuda include cheyyali ee main urls lo so adhi 
    #cheyyadaniki Manam Include Function ni vadatam 
    
    path('admin/', admin.site.urls),

]
