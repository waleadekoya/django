import os
from threading import Thread
import sys
from logger import Logger

sys.path.append("django")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
import django

django.setup()

# DUMMY POPULATE SCRIPT
from users_app.models import User
from faker import Faker

fake = Faker()
log = Logger().log


def populate_db(no_of_entries):
    # Add person to the Database

    for _ in range(no_of_entries):
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_email = fake.email()

        # populate db with fake first_name, last_name, and email
        User.objects.create(first_name=fake_first_name,
                            last_name=fake_last_name,
                            email=fake_email)


if __name__ == '__main__':
    log.info("populating script...!")
    t = Thread(target=populate_db, args=(20,))
    t.start()
    log.info("populating completed!")
