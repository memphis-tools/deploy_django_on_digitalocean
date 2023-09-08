from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms


def signin(request):
    """
    Description: vue pour la page inscription
    Paramètre(s):
    - request: le paramètre par défaut indispensable
    """
    form = forms.TopBlogUserCreationForm()
    if request.method == "POST":
        form = forms.TopBlogUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, message=f"Bienvenue {user.username}, merci de vous connecter")
            return redirect("home")
        else:
            messages.error(request, message="Erreur de saisie")
    return render(request, "authentication/signin.html", context={"form": form})
