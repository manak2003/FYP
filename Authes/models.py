from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_pasword_token = models.CharField(max_length=100, default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

    
class Organization(models.Model):
    organization_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    website = models.CharField(max_length=100,default="", null=True, blank=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    phone = models.IntegerField()
    
    def __str__(self):
        return self.organization_name
