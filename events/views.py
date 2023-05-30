from django.shortcuts import render,redirect
from .forms import EventForm,  EventMemberForm, EventCategoryForm
from .models import Event,  EventMember, EventCategory
from django.contrib import messages
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def EventCategoryPage(request):
    return render(request, 'events/event_category.html')

def EventPage(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        category = form.cleaned_data['category']
        name = form.cleaned_data['name']
        image = form.cleaned_data['image']
        uid = form.cleaned_data['uid']
        description = form.cleaned_data['description']
        select_schedule_status = form.cleaned_data['select_schedule_status']
        scheduled_status = form.cleaned_data['scheduled_status']
        venue = form.cleaned_data['venue']
        start_date = form.cleaned_data['start_date']
        location = form.cleaned_data['location']
        maximum_participants = form.cleaned_data['maximum_participants']
        status_choice = form.cleaned_data['status_choice']
        status = form.cleaned_data['status']
        
        event = Event(category=category, name=name, image=image,uid=uid, description=description, select_schedule_status=select_schedule_status, scheduled_status=scheduled_status, venue=venue, start_date=start_date, location=location, maximum_participants=maximum_participants, status_choice=status_choice, status=status)
        event.save()
        
        messages.success(request, 'Event added successfully')
        return redirect('events')
    
    data = Event.objects.all()
    return render(request, 'events/event.html', {'data': data, 'form': form})


def EventMemberPage(request):
    return render(request, 'events/event_member.html')

def CreateEventPage(request):
    form = EventForm(request.POST , request.FILES or None)
    if form.is_valid():
        category = form.cleaned_data['category']
        name = form.cleaned_data['name']
        image = form.cleaned_data['image']
        uid = form.cleaned_data['uid']
        description = form.cleaned_data['description']
        select_schedule_status = form.cleaned_data['select_schedule_status']
        scheduled_status = form.cleaned_data['scheduled_status']
        venue = form.cleaned_data['venue']
        start_date = form.cleaned_data['start_date']
        location = form.cleaned_data['location']
        maximum_participants = form.cleaned_data['maximum_participants']
        status_choice = form.cleaned_data['status_choice']
        status = form.cleaned_data['status']
        
        event = Event(category=category, name=name, image=image,uid=uid, description=description, select_schedule_status=select_schedule_status, scheduled_status=scheduled_status, venue=venue, start_date=start_date, location=location, maximum_participants=maximum_participants, status_choice=status_choice, status=status)
        event.save()
        
        messages.success(request, 'Event added successfully')
        return redirect('events')
    
  
     
    data = Event.objects.all()
    return render(request, 'events/create_event.html', {'data': data, 'form': form})
    