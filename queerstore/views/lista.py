from django.shortcuts import render
from django.views.generic import ListView


class Inicio(ListView):
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})

class Camisetas(ListView):
    template = 'camisetas.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})


class Canecas(ListView):
    template = 'canecas.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})

class Contato(ListView):
    template = 'contato.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})