import os
from threading import Thread
import sys
from .logger import Logger

sys.path.append("django")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
import django

django.setup()

# DUMMY POPULATE SCRIPT
import random
from .abinitio_app.models import Company, Programmer, Language
from faker import Faker
log = Logger().log

fake = Faker()
companies_list = ['Microsoft', 'Intel', 'Apple', 'Facebook', 'Twitter', 'IBM', 'Google Inc.',
                  'Oracle', 'Accenture', 'SAP', 'TCS', 'Capgemini', 'Infosys', 'Cognizant',
                  'Dell Technology', 'LG', 'Panasonic', 'Sony']
languages_list = ['Python', 'Java', 'Ruby', 'Haskell', 'SQL',
                  'DotNet', 'HTML', 'Golang', 'Javascript', 'C++',
                  'C#', 'Swift', 'TypeScript', 'R', 'PHP',
                  'Perl', 'Lisp', 'Pascal', 'Scheme', 'Swift',
                  'Scala', 'Elixir', ]
creators_list = ['Guido van Rossum', 'James Gosling', 'Yukihiro Matsumoto', 'Philip Wadler', 'Donald Chamberlin',
                 'Microsoft', 'Tim Berners-Lee', 'Ken Thompson', 'Brendan Eich', 'Bjarne Stroustrup',
                 'Anders Hejlsberg', 'Chris Lattner', 'Microsoft', 'Ross Ihaka', 'Rasmus Lerdorf',
                 'Larry Wall', 'John McCarthy', 'Niklaus Wirth', 'Gerald Jay Sussman', 'Chris Lattner',
                 'Martin Odersky', 'José Valim']


def add_companies():
    # add new company to the database if not already existing
    try:
        companies = [Company.objects.get(comp_name=i) for i in companies_list]
    except Company.DoesNotExist:
        companies = [Company.objects.create(comp_name=i, location=fake.city(), date_created=fake.date())
                     for i in companies_list]

    # get the primary keys for each company in the database
    companies_pk_ids = [company.pk for company in companies]
    return companies, companies_pk_ids


def add_languages():
    lang_creator_dict = dict(zip(languages_list, creators_list))

    # add new language to the database if not already existing
    try:
        languages = [Language.objects.get(lang_name=lang_name) for lang_name, creator in lang_creator_dict.items()]
    except Language.DoesNotExist:
        languages = [
            Language.objects.create(lang_name=lang_name, creator=creator, paradigm='', date_created=fake.date())
            for lang_name, creator in lang_creator_dict.items()]

    # get the primary keys for each language in the database
    languages_pk_ids = [language.pk for language in languages]
    return languages, languages_pk_ids


def populate_db(no_of_entries):
    # Add companies to the Database
    companies, companies_pk_ids = add_companies()
    company_instances = [Company.objects.get(pk=pk) for pk in companies_pk_ids]

    # Add languages to the Database
    languages, languages_pk_ids = add_languages()
    language_instances = [Language.objects.get(pk=pk) for pk in languages_pk_ids]

    for _ in range(no_of_entries):
        # assign up to 5 languages for each programmer
        languages_set = random.choices(language_instances, k=random.choice([1, 2, 3, 4, 5]))
        log.info(languages_set)

        # get a company for each programmer
        company = random.choice(company_instances)

        # create a programmer and assign a company for each programmer
        fake_name = fake.name()
        fake_age = fake.random_int(min=25, max=45)
        programmer = Programmer.objects.create(programmer_name=fake_name, age=fake_age, company=company)
        programmer_pk_id = programmer.pk
        programmer_instance_object = Programmer.objects.get(pk=programmer_pk_id)

        # assign up to 5 languages to each programmer
        [programmer.languages.add(language) for language in languages_set]


if __name__ == '__main__':
    log.info("populating script...!")
    t = Thread(target=populate_db, args=(215,))
    t.start()
    log.info("populating completed!")
