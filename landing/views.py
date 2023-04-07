from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.conf import settings

def landing_page(request):
    return render(request, 'landing/landing_page.html')

