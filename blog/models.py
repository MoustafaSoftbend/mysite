from django.db import models 
from django.utils import timezone

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to='logo-image', blank=True)
    
    def __str__(self):
        return "logo-picture"
    
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text= models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date= models.DateTimeField(blank=True, null=True) 
    image = models.ImageField(upload_to='profile-image', blank=True)
    
    def __str__(self):
        return self.title