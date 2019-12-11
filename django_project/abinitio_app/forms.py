from django import forms
from abinitio_app.models import Company, Programmer, Language


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        # Option 1 - use "__all__" to add all fields to your form
        fields = "__all__"


class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer
        # Option 2 - use exclude to list fields to exclude in the form
        exclude = ["company"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        # Option 3 - list the fields to be added to your form
        fields = ["lang_name", "creator", "date_created"]
