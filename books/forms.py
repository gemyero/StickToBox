from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'placeholder': 'Type your Username','class':'full-width has-padding has-border','id':'signin-username'}), max_length=25)
    email = forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder': 'Type your Email','class':'full-width has-padding has-border','id':'signin-email'}),max_length=50)
    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={'placeholder': 'Type your Password','class':'full-width has-padding has-border','id':'signin-password'}),min_length=6)
    repass = forms.CharField(label="Re-type Password",widget=forms.TextInput(attrs={'placeholder': 'Re-type Password','class':'full-width has-padding has-border','id':'signin-repass'}),min_length=6)


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", widget=forms.TextInput(attrs={'placeholder': 'Type your Username','class':'full-width has-padding has-border','id':'signin-username'}), max_length=25)
    password = forms.CharField(label="Password", widget=forms.TextInput(attrs={'placeholder': 'Type your Password','class':'full-width has-padding has-border','id':'signin-password'}),min_length=6)