from django.urls import path
from . import views


urlpatterns = [
       path('subscribe/', views.Subscription, name='subscribe'),
       path('members/', views.members_view, name='members'),
       path('mhome/', views.mhome_view, name='mhome'),
       
]
