from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_pet', 'telefone', 'dia_reserva', 'observacoes']
        widgets = {
            'dia_reserva': forms.DateInput(attrs={'type': 'date'}),
        }
