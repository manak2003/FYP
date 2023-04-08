from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime as dt
from datetime import timedelta

# Create your models here.

## This is user settings model
class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_verified = models.BooleanField(default=False)
    verified_code = models.CharField(max_length=10, null=True, blank=True)
  ##  verification_expires = models.DateTimeField(default=dt.now().date() + timedelta(days=settings.VERIFY_EXPIRES_DAYS))
    code_expired = models.BooleanField(default=False)
    recieve_email_notice = models.BooleanField(default=True)

## This is user membership model
class Membership(models.Model):
    MEMBERSHIP_CHOICES = (('Extended','Extended'), ('Advance','Advance'),('Medium','Medium'),('Basic','Basic'),('Free','Free'))
    
    PERIOD_DURATION = (('Days','Days'), ('Week','Week'), ('Months','Months '), ('Year','Year'))
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, max_length=30, default='Free')
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(choices=PERIOD_DURATION, max_length=30, default='Days')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    
    def __str__(self):
        return self.membership_type
    
## User membership model
class UserMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True, blank=True,related_name='user_membership')
    
    def __str__(self):
        return self.user.username  
    
# @reciever(post_save, sender=UserMembership)
# def create_subscription(sender, instance, *args, **kwargs):
#     if instance:
#         Subscription.objects.create(user_membership=instance, expires_in=dt.now().date() + timedelta(days=instance.membership.duration))  

## User subscription model
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, on_delete=models.CASCADE, related_name='user_subscription')
    expires_in = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user_membership.user.username
    
## User payment history model
class PayHistory(models.Model):
    user_membership = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    payment_for = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user_membership.user.username