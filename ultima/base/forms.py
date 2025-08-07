from django import forms
from base.models import Contato

class InscreverForm(forms.Form):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'observacao']

class ContatoForm(forms.Form):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']