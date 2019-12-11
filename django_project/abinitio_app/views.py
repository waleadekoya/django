from django.db.models import QuerySet
from django.shortcuts import render
from abinitio_app.models import Programmer
from abinitio_app.tasks import send_mail_task
from . import forms

# Create your views here.


def home(request):
    # makes the index view as the home page
    # context = {'home_me': "Thanks for visiting my website. See you soon"}

    # connecting views with models (our database) using MVT design architecture
    programmers_list = Programmer.objects.order_by('company')
    programmer_dict = {'programmers':  programmers_list}
    # intel_programmers = Company.objects.get(comp_name='Intel').programmer_set.all()
    # languages = Language.objects.all()
    # print([i.pk for i in intel_programmers])
    # https://docs.djangoproject.com/en/dev/ref/models/querysets/#values
    # https://stackoverflow.com/questions/4424435/how-to-convert-a-django-queryset-to-a-list
    # print([programmer.languages.all() for programmer in programmers_list])
    # print([programmer.languages.values('lang_name') for programmer in programmers_list])
    # languages = [programmer.languages.values_list('lang_name', flat=True) for programmer in programmers_list]
    # print([language for language in languages])
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
        print('From Validation Success. Prints in console')
        print('Name: '+form.cleaned_data['comp_name'])
        print('Email: '+form.cleaned_data['location'])
        print('Text: '+form.cleaned_data['date_created'])
    return render(request, 'abinitio_app/forms.html', {'form': form})


