from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField


# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    location = models.CharField(max_length=100)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    neighborhood = models.ForeignKey("NeighborHood", on_delete=models.CASCADE, null=True)
    profile_pic = CloudinaryField('image', null=True)

    def __str__(self):
          return f'{self.user} Profile'
    def save_profile(self):
        self.save
    def delete_profile(self):
        self.delete()

   
    @classmethod
    def get_profile(cls, id):
        profile = cls.objects.get(id=id)
        return profile

class NeighborHood(models.Model):
    image=  CloudinaryField('image', null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey("Profile", on_delete=models.CASCADE, null=True, related_name = 'hood')
    occupants = models.ManyToManyField(User, related_name='neighborhoods')

    def __str__(self):
        return self.name
    def delete_neighborhood(self):
        self.delete()
   
    @classmethod
    def get_neighborhood(cls, id):
        neighborhood = cls.objects.get(id=id)
        return neighborhood
    def update_neighborhood(self):
        self.save()
    def update_occupants_count(self):
        self.occupants_count = self.occupants.count()
        self.save()
    def create_neighborhood(self):
        self.save()    
    @classmethod
    def search_by_hood(cls, search_term):
        neighborhood = cls.objects.filter(name__icontains=search_term)
        return neighborhood


class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    location = models.CharField(max_length=100)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey("NeighborHood", on_delete=models.CASCADE, null=True)
    profile_pic = CloudinaryField('image', null=True)

    def __str__(self):
        return self.name        
    def create_business(self):
        self.save()
    def delete_business(self):
        self.delete()
    def update_business(self):
        self.save()
    @classmethod
    def search_by_business(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null=True)
    image = CloudinaryField('image', null=True)

    def __str__(self):
        return self.title
    def save_post(self):
        self.save()
    def delete_post(self):
        self.delete()
    @classmethod
    def search_by_post(cls, search_term):
        post = cls.objects.filter(title__icontains=search_term)
        return post