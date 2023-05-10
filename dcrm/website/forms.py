from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'first-name', 'placeholder':'First Name', 'autocomplete': 'off'}))
    last_name = forms.CharField(label="", max_length="50", widget=forms.TextInput(attrs={'class': 'last-name', 'placeholder':'Last Name', 'autocomplete': 'off'}))
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'email', 'placeholder': 'Email Address', 'autocomplete': 'off'}))



    class Meta:
        model = User

        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'username'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].widget.attrs['autocomplete'] = 'off'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="notice">Think of something different. Same usernames will be rejected.</span>'

        self.fields['password1'].widget.attrs['class'] = 'password1'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = ''

        self.fields['password2'].widget.attrs['class'] = 'password2'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="notice">Passwords must match.</span>'



class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'First Name', 'class': 'first-name'}), label="")
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Last Name', 'class': 'last-name'}), label="")
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email', 'class': 'email'}), label="")
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Phone", "class": "phone"}), label="")
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Address', 'class': 'address'}), label="")
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'City', 'class': 'city'}), label="")
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'state'}), label="")
    zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'State', 'class': 'state'}), label="")


    class Meta:
        model = Record
        exclude = ("user",)