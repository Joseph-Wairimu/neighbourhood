from django.urls import path,register_converter,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    

]




