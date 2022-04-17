from django.urls import path,register_converter,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    
      path('',views.index,name='index'),
      path('nyumba/profile/', views.profile, name='profile'),
      path('nyumba/edit_profile/', views.edit_profile, name='edit_profile'),
      path('nyumba/hoods/', views.hoods, name='hoods'),
      path('nyumba/add_hood/', views.add_hood, name='add_hood'),
      path('nyumba/business/', views.business, name='business'),
      path('nyumba/add_business/', views.add_business, name='add_business'),
      path('joinhood/<id>', views.joinhood, name='joinhood'),
      path('leavehood/<id>', views.leavehood, name='leavehood'),
      path('singlehood/<id>', views.singlehood, name='singlehood'),
      path('nyumba/search/', views.search_business, name='search_business'),
      path('nyumba/search_hood/', views.search_hood, name='search_hood'),
      path('nyumba/post/', views.post, name='post'),
      path('nyumba/single_post/<id>', views.single_post, name='single_post'),
      path('nyumba/single_business/<id>/', views.single_business, name='single_business'),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




