from celery import shared_task
from django.core.mail import send_mail
from smtplib import SMTPException

from accounts.tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string


@shared_task
def send_user_email(user, template_obj):
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


@shared_task
def send_welcome_email(user):
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
    

@shared_task
def send_email_to_user(mail_subject, recipient_email, message):
    try:
        send_mail(
        mail_subject,
        None,
        'bestnaijaclips@gmail.com',
        [recipient_email],
        html_message=message,
        fail_silently=False)
        return True
    except SMTPException as e:
        print(str(e))
        return False
    except Exception as e:
        print(str(e))
        return False