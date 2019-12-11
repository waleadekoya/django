import sys
import os
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
from django.shortcuts import render
from abinitio_app.models import Programmer
from abinitio_app.tasks import send_mail_task
from abinitio_app import forms

from logger import Logger

# Create your views here.

log = Logger().log


def home(request):
    # connect views with data models using MVT design architecture
    programmers_list = Programmer.objects.order_by('company')
    programmer_dict = {'programmers': programmers_list}
    return render(request, "abinitio_app/home.html", programmer_dict)


def index(request):
    send_mail_task.delay()
    context = {'insert_me': "Email sent with Celery!"}
    # template = loader.get_template('abinitio_app/index.html')
    return render(request, 'abinitio_app/index.html', context)


def help(request):
    context = {'help_insert': "HELP PAGE"}
    return render(request, 'abinitio_app/help.html', context)


def form_name_view(request):
    form = forms.CompanyForm()
    # Check to see if we get a POST back
    if request.method == 'POST':
        # then we pass in that request
        form = forms.CompanyForm(request.POST)
    # Check if form is valid
    if form.is_valid():
        # Do the following (take an action)
        log.info('From Validation Success. Prints in console')
        log.info('Name: ' + form.cleaned_data['comp_name'])
        log.info('Email: ' + form.cleaned_data['location'])
        log.info('Text: ' + form.cleaned_data['date_created'])
    return render(request, 'abinitio_app/forms.html', {'form': form})
