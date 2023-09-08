from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    """
    Description: vue pour la page accueil.
    Paramètre(s):
    - request: le paramètre par défaut indispensable
    """
    return render(request, "topblog/home.html")
