from django.db import models

# You can use the Faker python library to populate your model with dummy data.
# Create your models here.


class Company(models.Model):
    comp_name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(null=True)

    def __str__(self):
        return self.comp_name


class Language(models.Model):
    lang_name = models.CharField(max_length=255, unique=True)
    creator = models.CharField(max_length=255, null=True)
    paradigm = models.CharField(max_length=255, null=True)
    date_created = models.DateField(null=True)

    def __str__(self):
        return self.lang_name


class Programmer(models.Model):
    programmer_name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.programmer_name

