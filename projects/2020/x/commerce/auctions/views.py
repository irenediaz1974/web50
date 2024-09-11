from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Producto_form, Categoria_form, Imagen_form, Subasta_form
from .models import User , Producto , Subasta
from django.forms import inlineformset_factory


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
       
    #subasta_form=Subasta_form()
    subasta_instance = Subasta.objects.create(s_estado=True, id_user=request.user)
    subasta_form = Subasta_form(instance=subasta_instance)
    formset = ProductoFormSet(instance=subasta_instance)
    return render(request, "auctions/add_subasta.html", {'subasta_form': subasta_form, 'formset': formset})


    #return render(request, "auctions/add_subasta.html", {'subasta_form': subasta_form})
    


# Vista para implementar producto
def add_producto(request):
    if request.method == 'POST': 
        categ_form = Categoria_form(request.POST, prefix='categ')
        prod_form = Producto_form(request.POST, prefix='prod')
        imagen_form = Imagen_form(request.POST, request.FILES, prefix='imagen')

        if categ_form.is_valid():
            categoria = categ_form.save()
        
            if prod_form.is_valid():
                producto = prod_form.save(commit=False)
                producto.id_cat = categoria  # Asignar la categoría recién creada
                producto.save()
            
                if imagen_form.is_valid():
                    imagen = imagen_form.save(commit=False)
                    imagen.id_producto = producto  # Asignar el producto recién creado
                    imagen.save()
                
                return redirect('index')
            else:
                print(prod_form.errors)  # Imprime los errores de validación del producto
        else:
             print(categ_form.errors)  # Imprime los errores de validación de la categoría
 
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
