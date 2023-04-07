from django.urls import path
from . import views

urlpatterns = [
    path('transaction_list/', views.transaction_list, name='transaction_list'),
]