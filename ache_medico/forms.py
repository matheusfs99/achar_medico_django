from django import forms
from django.contrib.auth.models import User
from .models import *


class UsersForms(forms.ModelForm):
    User._meta.get_field('first_name').blank = False
    User._meta.get_field('last_name').blank = False
    User._meta.get_field('email').blank = False
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Sobrenome'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Usuário'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Senha'}),
        }
    def save(self, commit=True):
        user = super(UsersForms, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class MedicoForms(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['sexo', 'data_nascimento', 'telefone', 'especialidade', 'foto']
        widgets = {
            'sexo': forms.Select(choices=Sexo.SEXO, attrs={'class': 'form-control', 'style': 'border-radius: 2rem;height: 50px'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'maxlength': 9}),
            'telefone': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': 11, 'placeholder': 'Telefone'}),
            'especialidade': forms.Select(choices=Especialidade.ESPECIALIDADE,
                                          attrs={'class': 'form-control', 'style': 'border-radius: 2rem;height: 50px'}),
        }

class BioForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['bio']

class PlanosForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['planos_aceitos']
        widgets = {
            'planos_aceitos': forms.CheckboxSelectMultiple(choices=Plano_Saude.PLANO)
        }

class BuscaEspecialidadeForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ['especialidade']
        widgets = {
            'especialidade': forms.Select(choices=Especialidade.ESPECIALIDADE,
                                          attrs={'class': 'form-control', 'style': 'border-radius: 2rem;height: 50px'}),
        }