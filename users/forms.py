from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from users.models import User, Subscriber


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        ''' Validate Aalto email addresses. '''
        email = self.cleaned_data['email']
        if not email.endswith("@aalto.fi"):
            raise ValidationError(
                    "Please provide an Aalto email address."
                )
        return email

    class Meta:
        model = User
        fields = ['email', 'address']


class PrivacyForm(forms.ModelForm):
    privacy = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = ['privacy']


class ConsentForm(forms.ModelForm):

    # Consent consists of multiple questions. Add each here.
    widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    field_1 = forms.BooleanField(required=True, widget=widget)
    field_2 = forms.BooleanField(required=True, widget=widget)
    field_3 = forms.BooleanField(required=True, widget=widget)
    field_4 = forms.BooleanField(required=True, widget=widget)
    field_5 = forms.BooleanField(required=True, widget=widget)
    field_6 = forms.BooleanField(required=True, widget=widget)

    class Meta:
        model = User
        fields = ['consent']

    def clean(self):
        ''' If the form gets submitted, the user has consented to all the
            items. We can just set consent to true. '''
        cleaned_data = super().clean()
        cleaned_data['consent'] = True
        return cleaned_data


class SubscriptionForm(forms.ModelForm):
    email = forms.EmailField()

    def clean_email(self):
        ''' Validate Aalto email addresses. '''
        email = self.cleaned_data['email']
        if not email.endswith("@aalto.fi"):
            raise ValidationError(
                    "Please provide an Aalto email address."
                )
        return email

    class Meta:
        model = Subscriber
        fields = ['email']