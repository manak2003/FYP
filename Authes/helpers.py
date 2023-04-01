from django.core.mail import send_mail
from django.core import mail
import uuid
from django.conf import settings
from django.core.mail import BadHeaderError

def send_forget_password_mail(email, token):
    subject = 'Your forget password link'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/change_password/{token}/'
    from_email = settings.EMAIL_HOST_USER
    auth_user = settings.EMAIL_HOST_USER
    auth_password = settings.EMAIL_HOST_PASSWORD
    print(from_email)
    recipient_list = [email]
    try:
        with mail.get_connection(
            host=settings.EMAIL_HOST,
            port=settings.EMAIL_PORT,
            username=auth_user,
            password=auth_password,
            use_tls=settings.EMAIL_USE_TLS,
        ) as connection:
            email = mail.EmailMessage(
                subject, message, from_email, recipient_list, connection=connection
            )
            email.send()
    except BadHeaderError as e1:
        return f'invalid header found {e1}'
    return 'success'
        