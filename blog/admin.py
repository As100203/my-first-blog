from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)#we register our model to make it visible to admin

