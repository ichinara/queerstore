from django.shortcuts import render
from django.views.generic import ListView


class Inicio(ListView):
    template = 'home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template, {})
