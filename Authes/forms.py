from django import forms
from django.contrib.auth.models import User


INVALID_USERNAMES = ['admin','administrator','root']

# login form
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username

# register form
class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(help_text='Enter a valid email address')
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if qs.exists():
            raise forms.ValidationError("Username is not available!")
        if username.lower() in INVALID_USERNAMES:
            raise forms.ValidationError("Username is invalid")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        return email
    
class ForgetPasswordForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return username
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        qs = User.objects.filter(password__iexact=password)
        if not qs.exists():
            raise forms.ValidationError("Invalid Credentials")
        return password

class OrganizationForm(forms.Form):
    organization_name = forms.CharField()
    organization_email = forms.EmailField(help_text='Enter a valid email address')
    address = forms.CharField()
    phone = forms.CharField()
    website = forms.CharField()
    organization_logo = forms.ImageField()
    organization_description = forms.CharField()
    organization_type = forms.CharField()
    organization_country = forms.CharField()
    organization_state = forms.CharField()
    organization_city = forms.CharField()
    organization_zipcode = forms.CharField() 
    organization_status = forms.CharField()
    
    def clean_organization_name(self):
        organization_name = self.cleaned_data.get('organization_name')
        qs = Organization.objects.filter(organization_name__iexact=organization_name)
        if qs.exists():
            raise forms.ValidationError("Organization name is not available!")
        return organization_name
