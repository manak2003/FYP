from django.urls import path
from . import views

urlpatterns = [
    path('event_category/', views.EventCategoryPage, name='event_category'),
    path('event/', views.EventPage, name='events'),
    path('event_image/', views.EventImagePage, name='event_image'),
    path('event_member/', views.EventMemberPage, name='event_member'),
    
]