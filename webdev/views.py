#  hello/views.py
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Utilizador
from .forms import Utilizador_Form

def layout_page_view(request):
    form = Utilizador_Form(request.POST or None)
    context = {'form': form,
               'utilizadores': Utilizador.objects.all()}
    if form.is_valid():
        form.save()
        return render(request, 'webdev/layout.html', context)



    return render(request, 'webdev/layout.html', context)

def edit_page_view(request, utilizador_id):
    utilizador = Utilizador.objects.get(id=utilizador_id)
    form = Utilizador_Form(request.POST or None, instance=utilizador)
    context = {'form': form,
               'utilizadores': Utilizador.objects.all(),
               'main_utilizador': utilizador}
    if form.is_valid():
        form.save()
        return render(request, 'webdev/layout.html', context)

    return render(request, 'webdev/editar.html', context)