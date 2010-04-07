from django.conf import settings
from django import forms

#from .models import 

#import re

class ExampleForm(forms.Form):
    test = forms.CharField(required = False, max_length = 140, label = 'Test')

    def clean_test(self):
        test = self.cleaned_data['test']
        
        #Do something with test. If fail:
        raise forms.ValidationError(
                'There was an error with test' 
              )
        
        #If success:
        return test
