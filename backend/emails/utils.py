from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from smtplib import SMTPException
from .models import EmailTemplate, EmailTemplateType
from utils.utils import get_object_or_None
import random
import string
from django.template.loader import render_to_string #render template to string
from accounts.tokens import account_activation_token, login_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from accounts.tasks import send_email_to_user

def EmailReplace(template, key_dict:dict):
    key_list = list(key_dict.keys())

    for item in key_list:
        if dict[item] is None:
            dict[item] = ''

        template = template.replace("["+item+"]", dict[item])

    return template


def email_user(user, template_obj):
    user_email = user.email
    subject = template_obj['title']
    message = template_obj['message']
    emails = template_obj['emails']
    try:
        send_mail(
        subject,
        None,
        'CourseConnect <noreply@courseconnect.com>',
        emails,
        html_message=message,
        fail_silently=True)
        # return True
    except SMTPException as e:
        print(str(e))
    except Exception as e:
        print(str(e))
    
    
    # email = EmailMessage(subject, message, to=emails)
    # if email.send():
    #     return True
    # else:
    #     return False
    
def email_user_template(request, template_name):
    user = request.user
    link = request.build_absolute_uri()
    template = EmailTemplate.objects.get(type=template_name)
    key_dict = {
        "user_name": 'some_user_name',
        "verification_link": 'some_verification_link'
    }
    message = EmailReplace(template.message, key_dict)
    subject = EmailReplace(template.title, key_dict)
    #"protocol": 'https' if request.is_secure() else 'http'
    #'token': account_activation_token.make_token(user)
    #'domain: get_current_site(request).domain
    #render_to_string("template.html", {'user_name': username, })
    #'protocol': 'https' if request.is_secure() else 'http'

def MatchKeyGenerator(length):
    # Select the characters to choose from
    characters = string.ascii_letters

    # Generate a random string of specified length
    random_string = ''.join(random.choice(characters) for _ in range(length))

    return random_string


def welcome_email(user, ):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    mail_subject = "Activate Your user account."
    activation_link = f"http://127.0.0.1:3000/activate/{uid}/{token}"
    message = render_to_string("emails/template_welcome_user.html", {
        "user": user.email,
        "activation_link": activation_link
    })
    try:
        send_mail(
        mail_subject,
        None,
        'bestnaijaclips@gmail.com',
        [user.email],
        html_message=message,
        fail_silently=False)
        return True
    except SMTPException as e:
        print(str(e))
        return False
    except Exception as e:
        print(str(e))
        return False
    

def send_login_link(user):
    token = login_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    login_link = reverse('login-link', kwargs={'uidb64': uid, 'token': token})
    login_url = f"{settings.SITE_URL}{login_link}"

    subject = "Your Login Link"
    message = f"Hi {user.username},\n\nClick the link below to log in:\n\n{login_url}\n\nThis link will expire in 24 hours."
    send_mail(subject, None, settings.DEFAULT_FROM_EMAIL, [user.email], html_message=message)

def send_welcome_email_async(user):
    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    mail_subject = "Activate Your user account."
    activation_link = f"http://127.0.0.1:3000/activate/{uid}/{token}"
    message = render_to_string("emails/template_welcome_user.html", {
        "user": user.email,
        "activation_link": activation_link
    })
    send_email_to_user.delay(
        mail_subject, user.email, message
    )