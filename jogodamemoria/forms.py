from django import forms

from jogodamemoria.models import ControlePartida


class CriaUsuarioForm(forms.Form):
    newuser = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    newmail = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    newpass = forms.CharField(required=True, widget=forms.PasswordInput())
    newpass2 = forms.CharField(required=True, widget=forms.PasswordInput())


class CriaSalaForm(forms.ModelForm):
    class Meta:
        model = ControlePartida
        fields = ['tipo_partida', 'level_partida', 'nome_partida']
