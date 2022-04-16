from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class NeighborHood(models.Model):
    image=  CloudinaryField('image', null=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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




class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    location = models.CharField(max_length=100)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null=True)
    profile_pic = CloudinaryField('image', null=True)

    def __str__(self):
        return self.name
    def edit_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()
    def create_profile(self):
        self.save()
    def update_profile_pic(self):
        self.save()
   
    @classmethod
    def get_profile(cls, id):
        profile = cls.objects.get(id=id)
        return profile
class Business(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)  
    location = models.CharField(max_length=100)
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, null=True)
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
    def get_business(cls, id):
        business = cls.objects.get(id=id)
        return business

