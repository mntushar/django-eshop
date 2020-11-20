from django import forms


#user loging form
class UserLogingForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Your User Email Id", 'required':'True'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':"Enter Password", 'required':'True'}))