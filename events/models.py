from django.db import models


# Create your models here.

class EventCategory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='event_category', blank=True, null=True)
    priority = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)    
    
    status_choice = ((True, 'Active'), (False, 'Inactive'))
    status = models.BooleanField(choices=status_choice ,default=True)
    
    def __str__(self):
        return self.name
    
class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='event_category')
    name = models.CharField(max_length=100)
    uid = models.PositiveIntegerField(unique=True)
    description = models.TextField()
    select_schedule_status = (('yet to scheduled', 'Yet to Scheduled'), ('scheduled', 'Scheduled'))
    scheduled_status = models.CharField(max_length=100, choices=select_schedule_status, default='yet to scheduled')
    venue = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    points = models.PositiveIntegerField()
    maximum_participants = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status_choice = (('active','Active'), ('disabled','Disabled'), ('completed','Completed'), ('cancelled','Cancelled'), ('deleted','Deleted'), ('expired','Expired'),('timeout','Time Out'))
    status = models.CharField(max_length=100, choices=status_choice, default='active')
    
    def __str__(self):
        return self.name

    
class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_image')
    image = models.ImageField(upload_to='event_image', blank=True, null=True)
    
    def __str__(self):
        return self.event.name
     
class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_member')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    attend_status_choice = (('waiting','Waiting'),
                     ('attending','Attending'),
                     ('completed','Completed'),
                     ('cancelled','Cancelled'),
                     ('absent','Absent'),
                     ('deleted','Deleted'))
    
    attend_status = models.CharField(max_length=100, choices=attend_status_choice, default='active')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status_choice =  (
        ('disabled', 'Disabled'),
        ('active', 'Active'),
        ('deleted', 'Deleted'),
        ('blocked', 'Blocked'),
        ('completed', 'Completed'),
    )
    status = models.CharField(max_length=100, choices=status_choice, default='active')
    
        
    def __str__(self):
        return self.event.name
        