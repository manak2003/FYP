from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from.views import login_view ,register_view,ForgetPassword,ChangePassword, home_view
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/',login_view, name ='login'),
    path('logout/',views.logout, name ='logout'),
    path('register/',register_view, name ='register'),
    path('home/',home_view, name ='home'),
    path('forget_password/', views.ForgetPassword, name ='forget_password'),
    path('change_password/<str:token>/', views.ChangePassword, name ='change_password'),
    
   
    
    # todo logout url 
]

urlpatterns += staticfiles_urlpatterns()