from django.shortcuts import render
from base.forms import InscreverForm, ContatoForm
from base.models import Contato
from eventos.models import Categoria

def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'Título Legal 1',
            'categoria': 'Categoria 1',
            'data': '30/08/2022'
        }
    )
    dados.append(
        {
            'titulo': 'Título Legal 2',
            'categoria': 'Categoria 2',
            'data': '29/08/2022'
        }
    )
    contexto = {
        'dados': dados,
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta

def contato(request):
    sucesso = False
    if request.method == 'GET':
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST or None)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Maria da Silva Pereira',
        'form': form,
        'sucesso': sucesso
    }
    return render(request, 'contato.html', contexto)

def inscrever(request):
    contexto = {'sucesso': False}
    form = InscreverForm(request.POST or None)
    if form.is_valid():
        form.save()
        contexto['sucesso'] = True
    contexto['form'] = form
    return render(request, 'inscrever.html', contexto)