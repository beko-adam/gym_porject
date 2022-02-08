from django.forms import ModelForm

from .models import Mumber

class Meumber_Form(ModelForm):

     class Meta:
    
        model = Mumber
        fields = '__all__'
        exclude = ('owner',)


class Meumber_Form_sub(ModelForm):

     class Meta:
    
        model = Mumber
        fields = ('name', 'money', 'data_sub',)
