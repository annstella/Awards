from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50, default= ' new bio ' )
    profile_pic = models.ImageField(upload_to='profile/' , default = 'default.jpg' )