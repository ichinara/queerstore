"""queerstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
#from django.urls import path
from queerstore.views.lista import Inicio, Camisetas, Canecas, Contato
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [

    url(r'^home/', Inicio.as_view()),
    url(r'^camisetas/', Camisetas.as_view()),
    url(r'^canecas/', Canecas.as_view()),
    url(r'^contato/', Contato.as_view()),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    # path('', application.urls),  # > Django-2.0
]