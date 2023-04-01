from django import forms
from .models import Event, EventImage, EventMember, EventCategory

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('category', 'name', 'uid', 'description', 'venue', 'start_date', 'end_date', 'location', 'points', 'maximum_participants', 'status')
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
class EventImageForm(forms.ModelForm):
    class Meta:
        model = EventImage
        fields = ('image',)
        
class EventMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ('attend_status',)

class  EventCategoryForm(forms.ModelForm):
    class Meta:
        model = EventCategory
        fields = ('name', 'description', 'status')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        