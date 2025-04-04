from django import forms # forms is a module in django 


class ApplicationForm(forms.Form): # We are inherenting from the form class        
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()
    date = forms.DateField()
    occupation = forms.CharField(max_length=80)