from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'placeholder': 'Type your Username','class':'form-control','id':'email-signup'}), max_length=25)
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'email@example.com','class':'form-control','id':'email-signup'}),max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Type your Password','class':'form-control','id':'password-signup'}),min_length=6)
    repass = forms.CharField(label="Retype Password",widget=forms.PasswordInput(attrs={'placeholder': 'Retype Password','class':'form-control','id':'password-confirm-signup'}),min_length=6)
    img = forms.ImageField(label="Profile Picture")

class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'placeholder': 'Type your Username','class':'form-control','id':'email-login'}), max_length=25)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Type your Password','class':'form-control','id':'password'}),min_length=6)