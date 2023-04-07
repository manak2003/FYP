from django.db import models

# Create your models here.
class Transaction(models.Model):
    # id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    def __str__(self):
        return self.description
    
