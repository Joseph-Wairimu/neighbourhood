from django.urls import path,register_converter,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
      path('',views.index,name='index'),
      path('nyumba/profile/', views.profile, name='profile'),
      path('nyumba/edit_profile/', views.edit_profile, name='edit_profile'),
    

]





