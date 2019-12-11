from celery import shared_task
from time import sleep
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.template import Engine, Context


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    # https://docs.djangoproject.com/en/2.2/topics/email/
    # sleep(10)
    recipients = ['chezyfive@yahoo.com',
                  'adekoya.wale@yahoo.com']
    subject1 = 'subject1'
    subject2 = 'subject2'

    message1 = 'PoC for sending emails with Celery in your django project x 2'
    message2 = 'PoC for sending emails with Celery_updated with new methods'
    mail1 = (subject1, message1, 'adekoya.wale@yahoo.com', recipients)
    mail2 = (subject2, message2, 'adekoya.wale@yahoo.com', recipients)
    # send_mail(subject=subject,
    #           message=message,
    #           from_email='adekoya.wale@yahoo.com',
    #           recipient_list=['adekoya.wale@yahoo.com'])
    # (a, b,) = [(subject, message, 'adekoya.wale@yahoo.com', [recipient]) for recipient in recipients]
    send_mass_mail((mail1, mail2), fail_silently=False)



