from django import forms
from .models import Event,  EventMember, EventCategory

class EventForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=EventCategory.objects.all(), empty_label="Select Category")
    name = forms.CharField(max_length=100)
    image = forms.ImageField()
    uid = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    select_schedule_status = (('yet to scheduled', 'Yet to Scheduled'), ('scheduled', 'Scheduled'))
    scheduled_status = forms.ChoiceField(choices=select_schedule_status, initial='yet to scheduled')
    venue = forms.CharField(max_length=100)
    start_date = forms.DateTimeField()
    location = forms.CharField(max_length=100)
    maximum_participants = forms.IntegerField()
    status_choice = (('active','Active'), ('disabled','Disabled'), ('completed','Completed'), ('cancelled','Cancelled'), ('deleted','Deleted'), ('expired','Expired'),('timeout','Time Out'))
    status = forms.ChoiceField(choices=status_choice, initial='active')
    
    class Meta:
        model = Event
        fields = ('category', 'name', 'image','uid', 'description', 'venue', 'start_date', 'end_date', 'location', 'points', 'maximum_participants', 'status')
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        

        
class EventMemberForm(forms.ModelForm):
    event = forms.ModelChoiceField(queryset=Event.objects.all(), empty_label="Select Event")
    created_date = forms.DateTimeField()
    updated_date = forms.DateTimeField()
    attentd_status_choice = (('waiting','Waiting'), ('attending','Attending'), ('completed','Completed'), ('cancelled','Cancelled'), ('absent','Absent'), ('deleted','Deleted'))
    attend_status = forms.ChoiceField(choices=attentd_status_choice, initial='waiting')
    status_choice =  ( ('disabled', 'Disabled'), ('active', 'Active'), ('deleted', 'Deleted'), ('blocked', 'Blocked'), ('completed', 'Completed'), )
    status = forms.ChoiceField(choices=status_choice, initial='active')
     
    class Meta:
        model = EventMember
        fields = ('attend_status',)

class  EventCategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    code = forms.CharField(max_length=100)
    image = forms.ImageField()
    priority = forms.IntegerField()
    created_date = forms.DateTimeField()
    updated_date = forms.DateTimeField()
    
    class Meta:
        model = EventCategory
        fields = ('name', 'description', 'status')
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        