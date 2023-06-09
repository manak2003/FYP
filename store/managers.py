from django.db import models
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime

from decimal import Decimal
CURRENCY = settings.CURRENCY

class OrderManager(models.Manager):

    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):

    def active(self):
        return self.filter(active=True)

    def have_qty(self):
        return self.active().filter(qty__gte=1)
    
    