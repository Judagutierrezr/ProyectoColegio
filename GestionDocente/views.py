from django.shortcuts import render, HttpResponse, redirect
from GestionDocente.models import Profesor,Curso
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import View
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, "GestionDocente/home.html")

def docente(request):
    profesor=Profesor.objects.all()
    return render(request, "GestionDocente/docente.html",{"profesor":profesor})
    

def estudiante(request):    
    return render(request, "GestionDocente/estudiante.html")

class Vregistro(View):    
    def get(self, request):
        form = UserCreationForm()
        return render(request, "GestionDocente/registro.html",{"form":form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('GestionDocente/home')

        else :
            pass


def logear(request):
    form=AuthenticationForm()
    return render(request, "GestionDocente/login.html",{"form":form})