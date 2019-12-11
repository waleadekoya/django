from django.urls import path, re_path

from abinitio_app import views

urlpatterns = [
    path(route='', view=views.home, name='home'),
    path(route='index', view=views.index, name='index'),
    path(route='help', view=views.help, name='help'),
    path(route='formpage/', view=views.form_name_view, name='form_name')

]

# https://docs.djangoproject.com/en/2.2/intro/tutorial01/


