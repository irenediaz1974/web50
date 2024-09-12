from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Producto_form, Categoria_form, Imagen_form, Subasta_form
from .models import User , Producto , Subasta, Imagen
from django.forms import inlineformset_factory
from django.contrib import messages


ProductoFormSet = inlineformset_factory(Subasta, Producto, form=Producto_form, extra=1)
    #  inline formset para manejar instancias de Producto en la subasta. 
    # inlineformset_factory es usada para generar clases formset para varios Productos en una subasta.


def index(request):
    return render(request, "auctions/index.html")

@login_required
def categories(request):
    if request.method == 'POST': 
        categ_form = Categoria_form(request.POST, prefix='categ')   
        if categ_form.is_valid():
            categoria = categ_form.save()
            messages.success(request, 'Category saved successfully!')
            return HttpResponseRedirect(reverse("categories"))
        else:
             print(categ_form.errors)  # Imprime los errores de validación de la categoría
        
    else: 
        categ_form= Categoria_form(prefix='categ')
        

    return render(request, "auctions/categories.html", {'categoria':categ_form})

# Vista para adicionar lista watchlist

@login_required
def add_watchlist(request):
    
    # TODO: adicionar el producto a alguna lista que tenga el usuario

    return HttpResponseRedirect(reverse("index"))



# Vista para implementar subasta
@login_required
def add_subasta(request): 
    DEFAULT_IMAGE_ID = 1 
    if request.method == 'POST':       
        subasta_form = Subasta_form(request.POST)
        if subasta_form.is_valid():
            subasta_instance = subasta_form.save(commit=False)
            subasta_instance.s_estado = True
            subasta_instance.id_user = request.user
            subasta_instance.save()       
            formset = ProductoFormSet(request.POST, instance=subasta_instance)
            if formset.is_valid():
                productos = formset.save(commit=False)
                for producto in productos:
                    if not producto.id_imagen:
                        # Assign a default image if none is provided
                        producto.id_imagen = Imagen.objects.get(pk=DEFAULT_IMAGE_ID)
                    producto.save()
                messages.success(request, 'Listing saved successfully!')
                return HttpResponseRedirect(reverse("add_subasta"))
            else:
                print(formset.errors)
        else:
            print(subasta_form.errors)
            formset = ProductoFormSet()
    else:
        subasta_form = Subasta_form()
        formset = ProductoFormSet()
    
    return render(request, "auctions/add_subasta.html", {'subasta_form': subasta_form, 'formset': formset})




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
