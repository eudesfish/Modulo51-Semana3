from django.shortcuts import render
from .forms import ReservaForm

def reserva_pet(request):
    sucesso = False
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            form = ReservaForm()  # limpa o form
    else:
        form = ReservaForm()
    return render(request, 'reserva.html', {'form': form, 'sucesso': sucesso})
