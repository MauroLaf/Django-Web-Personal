from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    projects = Project.objects.all() #object es como una lista que gesitona en tiempo de ejecucion es automatico cuando se ejecuta django
    return render(request, "portfolio/portfolio.html", {'projects':projects})#agregamos como parametro ademas un diccionario "context"