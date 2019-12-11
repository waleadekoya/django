from celery import shared_task
from time import sleep
from django.core.mail import send_mass_mail


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    recipients = ['dummy_email@yahoo.com',
                  'adekoya.wale@yahoo.com']
    subject1 = 'subject1'
    subject2 = 'subject2'

    message1 = 'PoC for sending emails with Celery in your django project x 2'
    message2 = 'PoC for sending emails with Celery_updated with new methods'
    mail1 = (subject1, message1, 'adekoya.wale@yahoo.com', recipients)
    mail2 = (subject2, message2, 'adekoya.wale@yahoo.com', recipients)
    send_mass_mail((mail1, mail2), fail_silently=False)



