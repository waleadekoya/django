from django.shortcuts import render
from users_app.models import User

# Create your views here.


def users(request):
    context = {'users': 'this is the users page'}
    users_list = User.objects.order_by('id')
    users_dict = {'users': users_list}
    return render(request, "users_app/users.html", context=users_dict)
