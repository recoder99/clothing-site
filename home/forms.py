from .models import User
from .models import PersonalInformation
from django.forms import ModelForm

class signup_form(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class pi_form(ModelForm):
    class Meta:
        model=PersonalInformation
        #<Variable Name>
        fields = ['Address', 'ContactNumber']
        #<Variable Name>:<Label>
        labels = {'Address':"Address", 'ContactNumber':"Contact Number"}