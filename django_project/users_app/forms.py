from django import forms
from django.core import validators

NOT_ALLOWED = r"[@_!#£$%^&*()<>?/\|}{~:]"


def check_for_symbols(value):
    if any([char in value for char in NOT_ALLOWED]):
        for char in value:
            if char in NOT_ALLOWED:
                raise forms.ValidationError('Special character "{}" not allowed in name field'.format(char))


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_symbols])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("EMAIL DO NO MATCH!")
