from django import forms
from abinitio_app.models import Company, Programmer, Language


class CompanyForm(forms.ModelForm):
    # https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/
    # Form Fields go here
    class Meta:
        model = Company
        # Option 1 - use "__all__" to include all fields in the form
        fields = "__all__"


class ProgrammerForm(forms.ModelForm):
    # Form Fields go here
    class Meta:
        model = Programmer
        # Option 2 - use exclude to list fields to exclude in the form
        exclude = ["company"]


class LanguageForm(forms.ModelForm):
    # Form Fields go here
    class Meta:
        model = Language      #
        # Option 3 - list the fields to include in the form
        fields = ["lang_name", "creator", "date_created"]
