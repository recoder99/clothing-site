from .models import User
from django.forms import ModelForm

class signup_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']