from django.shortcuts import redirect,render
from .forms import LoginForm,RegisterForm,ForgetPasswordForm
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from .helpers import send_forget_password_mail 
from Authes.models import Profile

User = get_user_model() # get the user model

@login_required(login_url='/login/')
def Home(request):
    return render(request,'home.html')


def login_page(request):
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect( '/')


# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data.get('username')
        pwd = form.cleaned_data.get('password')
        user = authenticate(request, username=uname, password=pwd)
        if user is not None:
            login(request, user)
            # request.session['is_user'] = True
            messages.success(request, 'Login Successful')
            return redirect("home")
        else:
            messages.error(request,'Wrong Credentials')   
    ctx = {'form': form,'title':'Login'} 
    return render(request, "Authes/login.html", ctx)

#register view
def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        if password1 == password2:
            user = User.objects.create_user(username,email,password1)
            user.save()
            messages.success(request,'Registeration Successful')
            return redirect("login") # redirect to home page
        else:
            messages.error(request, 'Passwords do not match!')
        if user is not None:
            login(request,user)
            messages.success(request, 'Login Successful')
            return redirect("home")    
        
    ctx = {'form':form, 'title':'Register'}
    return render(request, "Authes/register.html", ctx)

def home_view(request):
    return render(request, 'Authes/home.html')

import uuid
def ForgetPassword(request):
    form = ForgetPasswordForm(request.POST or None)  
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'No user found with this username.')
                return redirect("login")
            user_obj = User.objects.get(username=username)
            if user_obj:
                token = str(uuid.uuid4())
                profile_obj = Profile.objects.get(user = user_obj)
                profile_obj.forget_password_token = token 
                profile_obj.save()
                print(user_obj, user_obj.email, token)
                send_forget_password_mail(user_obj.email , token )
                messages.success(request, 'An email is sent.')
                return redirect("login")
            else:
                messages.error(request, 'No user found with this username.')
    except Exception as e:
        print(e)
    return render(request,'Authes/forget_password.html')


def ChangePassword(request, token ):
    context = {}
    try:
        profile_obj = Profile.objects.fiter(forget_password_token = token).first()
        context = {'user_id': profile_obj.user.id}
        
        if request.method == 'POST':
            new_password =  request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')
            
            if user_id is None:
                messages.success(request, 'No user id found.')
                return redirect(f'/change_password/{token}/')
            
            if new_password != confirm_password:
                messages.success(request, 'Both password should be equal.')
                return redirect(f'/change_password/{token}/')
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return redirect('login')

        print(profile_obj)
        
        context = {'user_id: profile_obj.user.id'}
        
    except Exception as e:
        print(e)
    return render(request, 'Authes/change_password.html', context)
