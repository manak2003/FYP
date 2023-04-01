from django.db import models
from django.conf import settings
from .managers import ProductManager, OrderManager
from django.db.models import Sum
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime
from django.utils import timezone
from decimal import Decimal 

# Create your models here.

CURRENCY = settings.CURRENCY

class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    
class Order(models.Model):
    date = models.DateField(default=datetime.datetime.now)
    title = models.CharField(blank=True, max_length=100)
    timestamp = models.DateField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    is_paid = models.BooleanField(default=True)
    
    objects = models.Manager()
    browser = OrderManager
    
    class Meta:
        ordering = ['-date']
    
    
    def save(self, *args, **kwargs):
        # order_items = self.order_items.all()
        # self.value = order_items.aggregate(Sum('total_price'))['total_price__sum'] if order_items.exists() else 0.00
        self.final_value = Decimal(self.value) - Decimal(self.discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'New Order'

    def get_edit_url(self):
        return reverse('update_order', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_order', kwargs={'pk': self.id})

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'

    def tag_discount(self):
        return f'{self.discount} {CURRENCY}'

    def tag_value(self):
        return f'{self.value} {CURRENCY}'

    @staticmethod
    def filter_data(request, queryset):
        search_name = request.GET.get('search_name', None)
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        queryset = queryset.filter(title__contains=search_name) if search_name else queryset
        if date_end and date_start and date_end >= date_start:
            date_start = datetime.datetime.strptime(date_start, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_end = datetime.datetime.strptime(date_end, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date_start, date_end)
            queryset = queryset.filter(date__range=[date_start, date_end])
        return queryset
    
class Product(models.Model):
    class StatusChoice(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLIC = 1, 'Public'
    status = models.IntegerField(choices=StatusChoice.choices, default=StatusChoice.DRAFT)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=100)
    slug = models.URLField(max_length=100)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    discount_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    qty = models.PositiveIntegerField(default=0)
    
    
    objects = models.Manager()
    broswer = ProductManager()

    class Meta:
        verbose_name_plural = 'Products'
    
    def save(self, *args, **kwargs):
        self.final_value = self.discount_value if self.discount_value > 0 else self.value
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'
    tag_final_value.short_description = 'Value'
       
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    qty = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    def __str__(self):
        return f'{self.product.title}'

    def save(self,  *args, **kwargs):
        self.final_price = self.discount_price if self.discount_price > 0 else self.price
        self.total_price = Decimal(self.qty) * Decimal(self.final_price)
        super().save(*args, **kwargs)
        self.order.save()

    def tag_final_price(self):
        return f'{self.final_price} {CURRENCY}'

    def tag_discount(self):
        return f'{self.discount_price} {CURRENCY}'

    def tag_price(self):
        return f'{self.price} {CURRENCY}'

@receiver(post_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    product = instance.product
    product.qty += instance.qty
    product.save()
    instance.order.save()
    
def save(self,  *args, **kwargs):
    self.final_price = self.discount_price if self.discount_price > 0 else self.price
    self.total_price = Decimal(self.qty) * Decimal(self.final_price)
    super('final_price','total_price').save(*args, **kwargs)
    self.order.save()
        
@receiver(post_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    product = instance.product
    product.qty += instance.qty
    product.save()
   
class Image(models.Model):
    image = models.ImageField(upload_to='articles/images/')
    caption = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return self.image.url
    
class Delivery(models.Model):
    title = models.CharField(max_length=100,default='Delivery')
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=10)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=True)
    last_modified = models.DateTimeField(default=True)

    def __str__(self):
        return self.title
    
class Settings(models.Model):
    title = models.CharField(max_length=100,default=True)
    logo = models.ImageField(upload_to='settings/images/',default=True)
    phone = models.CharField(max_length=100,default=True)
    email = models.EmailField(default=True)
    address = models.CharField(max_length=100,default='Address')
    currency = models.CharField(max_length=100,default='Currency')
    created_at = models.DateTimeField(default=True)
    last_modified = models.DateTimeField(default=True)

    def __str__(self):
        return self.title
  