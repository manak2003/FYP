from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
       path('memberships/', views.MembershipSelectView.as_view(), name='membership_list'),
]
