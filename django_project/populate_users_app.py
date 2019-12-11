import os
from threading import Thread
# https://stackoverflow.com/questions/45737387/django-settings-module-no-module-named
import sys

sys.path.append(r"C:\Users\Sesan\OneDrive\@Python_Projects\Django_Web_Framework")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
import django

django.setup()

# FAKE POPULATE SCRIPT
import random
from users_app.models import User
from faker import Faker

fake = Faker()


def populate_db(no_of_entries):
    # Add person to the Database

    for _ in range(no_of_entries):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        # populate db with fake first_name, last_name, and email
        users = User.objects.create(first_name=fake_first_name,
                                    last_name=fake_last_name,
                                    email=fake_email)


if __name__ == '__main__':
    print("populating script...!")
    t = Thread(target=populate_db, args=(20,))
    t.start()
    print("populating completed!")
