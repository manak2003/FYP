from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password1 = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)
    
    def __str__(self):
        return self.username
    def __str__(self):
        return self.email
    
    class Login(models.Model):
        username = models.CharField(max_length=100)
        password = models.CharField(max_length=100)
        
        def __str__(self):
            return self.username
        def __str__(self):
            return self.password


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_pasword_token = models.CharField(max_length=100, default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
    

    