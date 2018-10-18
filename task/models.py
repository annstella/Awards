from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=50, default= ' new bio ' )
    profile_pic = models.ImageField(upload_to='profile/' , default = 'default.jpg' )

    def __str__(self):
       return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def get_user_profile(cls ,username):
        profile = cls.objects.get(user = username )
        return profile

    @classmethod
    def search_profile(cls, query):
        profile = cls.objects.filter(user__username__icontains=query)
        return profile

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
     if created:
        Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
     instance.profile.save()

class Projects(models.Model):
    projects = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    url = models.TextField()
    user= models.ForeignKey(User)
    # post = HTMLField()
    # profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption

    def save_images(self):
        self.save()
    
    @classmethod
    def get_images(cls):
                images = Image.objects.all()
                return images

    @classmethod
    def get_projects_by_id(cls, id):
                project = Projects.objects.filter(user_id=id).all()
                return projects

class ProjectsMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    
class ProfileMerch(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    