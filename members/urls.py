from django.urls import path, include
from . import views

app_name = 'membership'
urlpatterns = [
       path('memberships/', views.MembershipSelectView.as_view(), name='membership_list'),

]

