from django.contrib import admin
from .models import Event , EventCategory, EventImage, EventMember

# Register your models here.
@admin.register(Event)
class EventAdminAdmin(admin.ModelAdmin):
    '''Admin View for EventAdmin'''

    list_display = ('category','name')
    
@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    '''Admin View for EventCategory'''

    list_display = ('name','code')
    
@admin.register(EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    '''Admin View for EventMember'''

    list_display = ('attend_status','event')
    
