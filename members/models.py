from django.db import models
from django.contrib.auth.models import User

# Create your models here.
MEMBERSHIP_CHOICES = (('Premium','prememium'), ('Free','free'))

class Membership(models.Model):
    slug = models.SlugField()
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=30,default='Free')
    price = models.IntegerField()
    def __str__(self):
        return self.membership_type
    
class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.user.username
    
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE,related_name='subscription')
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user_membership.user.username
    
    
