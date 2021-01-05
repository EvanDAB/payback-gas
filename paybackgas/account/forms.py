from django import forms

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

class SimpleCalculatorForm(forms.Form):
    mpg=forms.IntegerField(label='Miles Per Gallon')
    gasprice=forms.IntegerField(label='Gas Price')
    distance=forms.IntegerField(label='Distance')

# class MPGCalculatorForm(forms.Form):
    