from django import forms
from .models import Job, Resume
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title', 'company', 'description', 'requirements', 'salary', 'location', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-text'}),
            'company': forms.TextInput(attrs={'class': 'form-text'}),
            'description': forms.Textarea(attrs={'class': 'form-text'}),
            'requirements': forms.Textarea(attrs={'class': 'form-text'}),
            # 'salary': forms.IntegerField(attrs={'class': 'form-text'}),
            # 'salary': forms.FileField(widget=forms.FileInput(attrs={'class': 'rounded_list'})),
            'location': forms.TextInput(attrs={'class': 'form-text'}),
        }


class ResumeForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ('name', 'email', 'phone', 'summary', 'skills', 'experience', 'education', )

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-text'}),
            'email': forms.EmailInput(attrs={'class': 'form-text'}),
            'phone': forms.TextInput(attrs={'class': 'form-text'}),
            'summary': forms.Textarea(attrs={'class': 'form-text'}),
            'skills': forms.Textarea(attrs={'class': 'form-text'}),
            'experience': forms.Textarea(attrs={'class': 'form-text'}),
            'education': forms.Textarea(attrs={'class': 'form-text'}),
            # 'salary': forms.IntegerField(attrs={'class': 'form-text'}),
            # 'salary': forms.FileField(widget=forms.FileInput(attrs={'class': 'rounded_list'})),
            'location': forms.TextInput(attrs={'class': 'form-text'}),
        }


# class UserRegisterForm(UserCreationForm):
#     username = forms.CharField(
#         label='Имя пользователя',
#         widget=forms.TextInput(attrs={'class': 'form-control'})
#     )
#
#     password1 = forms.CharField(
#         label='Пароль',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#
#     password2 = forms.CharField(
#         label='Пароль',
#         widget=forms.PasswordInput(attrs={'class': 'form-control'})
#     )
#
#     secret_word = forms.CharField(
#         label='Секретное слово',
#         widget = forms.TextInput(attrs={'class':'form-control'})
#     )
#
#     class Meta:
#         model = User
#         fields = ('username', 'password1', 'password2')
#
# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(
#         label='Имя пользователя',
#         widget = forms.TextInput(attrs={'class':'form-control'})
#     )
#
#     password = forms.CharField(
#         label='Пароль',
#         widget=forms.PasswordInput(attrs={'class':'form-control'})
#     )
#
#     secret_word = forms.CharField(
#         label='Секретное слово',
#         widget = forms.TextInput(attrs={'class':'form-control'})
#     )
#
# class SearchForm(forms.Form):
#     query = forms.CharField()
