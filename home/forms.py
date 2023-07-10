from .models import User
from .models import PersonalInformation
from django.forms import ModelForm

class signup_form(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class pi_form(ModelForm):
    class Meta:
        model=PersonalInformation
        #<Variable Name>
        fields = '__all__'
        #<Variable Name>:<Label>
        labels = {'Address':"Address", 'ContactNumber':"Contact Number"}