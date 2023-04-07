from django.contrib import admin
from .models import Transaction

# Register your models here.
@admin.register(Transaction)
class Admin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'description', 'category', 'account')