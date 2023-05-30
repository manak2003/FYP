from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('event_category/', views.EventCategoryPage, name='event_category'),
    path('event/', views.EventPage, name='events'),
    path('create_event/',views.CreateEventPage, name='create_event'),
    path('event_member/', views.EventMemberPage, name='event_member'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

