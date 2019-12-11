from django.urls import path

from users_app import views

urlpatterns = [
    path(route='users', view=views.users, name='users')
]

