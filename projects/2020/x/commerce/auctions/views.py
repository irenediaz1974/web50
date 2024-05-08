from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ProductoForm, CategoriaForm, ImagenProductoForm
from .models import User


def index(request):
    return render(request, "auctions/index.html")

# Vistas para implementar las tareas

def add_producto(request):
    if request.method == 'POST':
        prod_form = ProductoForm(request.POST, prefix='prod')
        categ_form= CategoriaForm(request.POST, prefix='categ')
        imagen_prod= ImagenProductoForm(request.POST, prefix='imagen')
        if prod_form.is_valid():
            if 'categ-nombre' in request.POST and categ_form.is_valid():
                categ_form.save()
            if 'imagen-descripcion' in request.POST and imagen_prod.is_valid():
                imagen_prod.save()
            prod_form.save()
            return render(request, "auctions/add_producto.html", {'producto': prod_form, 'imagen': imagen_prod, 'categoria':categ_form})
    else:
        prod_form = ProductoForm()
        categ_form= CategoriaForm()
        imagen_prod=ImagenProductoForm()

    return render(request, "auctions/add_producto.html", {'producto': prod_form, 'categoria':categ_form, 'imagen':imagen_prod})



# Vistas que venian con el ejercicio

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
