from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def EventCategoryPage(request):
    return render(request, 'events/event_category.html')

def EventPage(request):
    return render(request, 'events/event.html')

def EventImagePage(request):
    return render(request, 'events/event_image.html')

def EventMemberPage(request):
    return render(request, 'events/event_member.html')
