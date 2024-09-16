from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Producto_form, Categoria_form, Imagen_form, Subasta_form, ImageFormSet
from .models import User , Producto , Subasta, Imagen
from django.forms import inlineformset_factory
from django.contrib import messages




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

@login_required
def add_product(request): 

     if request.method == 'POST':
        product_form = Producto_form(request.POST)
        image_formset = ImageFormSet(request.POST, request.FILES)
        

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            image_formset.instance = product
            image_formset.save()
            return redirect('success_url')
     else:
        product_form = Producto_form()
        image_formset = ImageFormSet()
      

     return render(request, 'auctions/products.html', {
        'product_form': product_form,
        'image_formset': image_formset
    })
   
        
      
   



# Vista para implementar subasta
@login_required
def add_subasta(request): 
    if request.method == "POST":
        subasta_form = Subasta_form(request.POST)
        producto_form = Producto_form(request.POST)
        imagen_form = Imagen_form(request.POST, request.FILES)

        if subasta_form.is_valid() and producto_form.is_valid() and imagen_form.is_valid():
            subasta_instance = subasta_form.save(commit=False)
            subasta_instance.s_estado = True
            subasta_instance.id_user = request.user
            subasta_instance = subasta_form.save()
            producto_instance = producto_form.save(commit=False)
            producto_instance.subasta = subasta_instance
            producto_instance.save()
            imagen_instance = imagen_form.save(commit=False)
            imagen_instance.producto = producto_instance
            imagen_instance.save()
            messages.success(request, 'Listing saved successfully!')
            return redirect("add_subasta")
        else:
            # If forms are not valid, render the form again with errors
            return render(request, "add_subasta", {
                "subasta_form": subasta_form,
                "producto_form": producto_form,
                "imagen_form": imagen_form
            })
    else:
        subasta_form = Subasta_form()
        producto_form = Producto_form()
        imagen_form = Imagen_form()
        return render(request, "auctions/add_subasta.html", {
            "subasta_form": subasta_form,
            "producto_form": producto_form,
            "imagen_form": imagen_form
        })



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
