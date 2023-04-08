from django.shortcuts import render
from django.views.generic import ListView
from members.models import UserMembership, Membership, Subscription

# Create your views here.
def Subscription(request):
    return render(request, 'members/subscribe.html')

def members_view(request):
    return render(request, 'members/members.html')