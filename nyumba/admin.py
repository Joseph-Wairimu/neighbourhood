from django.contrib import admin
from .models import Profile,Business,NeighborHood,Post

# Register your models here.

admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(NeighborHood)
admin.site.register(Post)

