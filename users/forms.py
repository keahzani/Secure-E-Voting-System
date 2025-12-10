from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    identification_number = forms.CharField(max_length=20, label="ID Number")
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, label="Role")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'identification_number', 'role']

    def clean_identification_number(self):
        id_number = self.cleaned_data.get('identification_number')
        if Profile.objects.filter(identification_number=id_number).exists():
            raise forms.ValidationError("This ID number is already in use.")
        return id_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
