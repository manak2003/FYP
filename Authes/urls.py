from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from.views import login_view ,register_view,forgotpwd_view
urlpatterns = [
    path('login/', login_view, name ='login'),
    path('register/', register_view, name ='register'),
    path('forgotpwd/', forgotpwd_view, name ='forgotpwd'),
    # todo logout url 
]

urlpatterns += staticfiles_urlpatterns()