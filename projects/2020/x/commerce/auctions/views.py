from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Producto_form, Categoria_form, Imagen_form, Subasta_form
from .models import User


def index(request):
    return render(request, "auctions/index.html")

# Vista para implementar subasta
def add_subasta(request):   
    subasta_form=Subasta_form()
    
    return render(request, "auctions/add_subasta.html", {'subasta_form': subasta_form})
    


# Vista para implementar producto
def add_producto(request):
    if request.method == 'POST':  
        categ_form= Categoria_form(request.POST, prefix='categ')
        print(categ_form.errors)
        if 'categ-nombre' in request.POST and categ_form.is_valid():
            print("Es valido formulario categoria" + str(categ_form.is_valid()))
            print("Es valido nombre categoria" + str('categ-nombre' in request.POST))
            categoria = categ_form.save()
        else:
            print(categ_form.errors)
        prod_form = Producto_form(request.POST, prefix='prod')
        print(prod_form.errors)
        if prod_form.is_valid():
            prod_form.save()
        else:
            print(prod_form.errors)
        imagen_form= Imagen_form(request.POST, request.FILES, prefix='imagen')
        print(imagen_form.errors)
        if 'imagen-descripcion' in request.POST and imagen_form.is_valid():
            print("Es valido la descripcion de la imagen" + str('imagen-descripcion' in request.POST))
            print("Es valido formulario imagen" + str(imagen_form.is_valid()))
            imagen = imagen_form.save(commit=False)
            imagen.id_producto = prod_form.instance.id
            imagen.save()
        else:
            print(imagen_form.errors)        
        return redirect('index')
    else:
        prod_form = Producto_form(prefix='prod')
        categ_form= Categoria_form(prefix='categ')
        imagen_form=Imagen_form(prefix='imagen')
        return render(request, "auctions/add_producto.html", {'producto': prod_form, 'categoria':categ_form, 'imagen':imagen_form})



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
