from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField

# Create your models here.
class NeighborHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    occupants_count = models.IntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    occupants = models.ManyToManyField(User, related_name='neighborhoods')

    def __str__(self):
        return self.name