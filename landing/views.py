from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.conf import settings

def landing(request):
    ctx = {}
    ctx['title'] = 'Welcome'
    return render(request, 'landing/landing.html', ctx)

