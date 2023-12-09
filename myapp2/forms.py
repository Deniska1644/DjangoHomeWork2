from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number', 'address']


class AddImage(forms.Form):
    id_image = forms.IntegerField(min_value=1, max_value=999)
    image = forms.ImageField()
