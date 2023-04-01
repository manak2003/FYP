from django.contrib import admin
from .models import Category, Product, Order, OrderItem,Image

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','status','active','created_at','last_modified','category', 'tag_final_value', 'qty']
    list_select_related = ['category']
    list_filter = ['active', 'category','status']
    search_fields = ['title','product_name']
    list_per_page = 50
    fields = ['active', 'title', 'status','category', 'qty', 'value', 'discount_value', 'tag_final_value']
    autocomplete_fields = ['category']
    readonly_fields = ['tag_final_value']
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ('title','date','timestamp','final_value','is_paid')
    list_filter = ('date','title')
    search_fields = ('title',)
    
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for OrderItem'''

    list_display = ('product','order','qty','price','final_price','total_price')
    list_filter = ('product',)
    search_fields = ('product',)
    
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    '''Admin View for Image'''

    list_display = ('image','caption','created_at')
    list_filter = ('image',)
    
# @admin.register(Delivery)
# class DeliveryAdmin(admin.ModelAdmin):
#     '''Admin View for Delivery'''
    
#     list_display = ('title','value','active','created_at','last_modified')
#     list_filter = ('title','active')
 
        
# @admin.register(Settings)
# class SettingsAdmin(admin.ModelAdmin):
#     '''Admin View for Settings'''

#     list_display = ('title','logo','email','phone','address','created_at','last_modified')
#     list_filter = ('title','email','phone','address')
#     search_fields = ('title','email','phone','address')
    
    