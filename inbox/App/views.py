from django.shortcuts import render
# Para incluir el path del login necesitamos importar 
from django.contrib.auth.decorators import login_required #LOGIN REQUERIDO PARA PAGINAS PRIVADAS
from django.views.decorators.cache import cache_control #DESTRUYE LA SECCION DESPUES DE SALIRTE
# Create your views here.

# FUNCION PARA PARA EL HOME PAGE (FRONTEND)
def home (request):
    return render(request,"home.html")
# FUNCION PARA EL INBOX (BACKEND)


@login_required(login_url="login")
@cache_control(no_cache=True, must_revalidate=True, no_store= True)
def inbox(request):
    return render(request,"inbox.html")