from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest 
from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from .forms import Producto_form, Categoria_form, Imagen_form, Subasta_form, Oferta_form, Coment_form
from .models import User , Producto , Subasta, Imagen, Watchlist, Oferta, Subastado, Comentario
from django.contrib import messages
from django.conf import settings
from django.db.models import Max, Subquery, OuterRef
import os



def index(request):

    productos = Producto.objects.filter(subasta__s_estado=True).select_related('subasta', 'id_imagen').values('id','p_nombre', 'p_descrip', 'p_monto_ini','id_imagen__imagen', 'subasta__s_fecha_ini')
    for producto in productos:
        producto['id_imagen__imagen'] = producto['id_imagen__imagen'].replace('media/', '')
    context = {
        'productos': productos,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, "auctions/index.html", context)
    

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
            subasta_instance.save()
            imagen_instance = imagen_form.save()
            imagen_instance.save()
            producto_instance = producto_form.save(commit=False)  
            producto_instance.subasta = subasta_instance
            producto_instance.id_imagen = imagen_instance
            producto_instance.save()
            
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


def products(request,producto_id): 
    try:
        producto = Producto.objects.get(id=producto_id)
        id_subasta=producto.subasta.pk
        id_user_subasta= Subasta.objects.get(pk=id_subasta).id_user
        es_dueno = (id_user_subasta == request.user)
        subasta = Subasta.objects.get(pk=producto.subasta.pk)
        comentarios = Comentario.objects.filter(id_producto=producto)
        try:
            max_bid = Oferta.objects.filter(id_subasta=producto.subasta).aggregate(Max('o_monto'))
        except:
            max_bid=False  
        is_in_watchlist = False 
        context = {
                    'producto': producto,
                    'oferta_form': Oferta_form(),
                    'coment_form': Coment_form(),
                    'max_bid': max_bid,
                    'is_in_watchlist': is_in_watchlist,
                    'MEDIA_URL': settings.MEDIA_URL,
                    'producto_id': producto_id,
                    'id_user_subasta':id_user_subasta,
                    'es_dueno': es_dueno,  
                    'comentarios': comentarios,             
                }
        is_in_watchlist = False
        if request.user.is_authenticated:
                is_in_watchlist = Watchlist.objects.filter(user=request.user, w_producto=producto_id).exists()
                context['is_in_watchlist'] = is_in_watchlist
                    
    except Producto.DoesNotExist:
             raise Http404("Producto no encontrado.")
    return render(request, 'auctions/products.html', context)

def add_watchlist(request, producto_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Producto, id=producto_id)
        Watchlist.objects.create(user=request.user, w_producto=product)
    return redirect('products', producto_id=producto_id)



def remove_watchlist(request, producto_id):
    if request.user.is_authenticated:
        product = Producto.objects.get(id=producto_id)
        Watchlist.objects.filter(user=request.user, w_producto=producto_id).delete()
    return redirect('products', producto_id=producto_id)

def place_bid(request, producto_id):
      if request.user.is_authenticated:
        product = get_object_or_404(Producto, id=producto_id)
        if request.method == "POST":
            form = Oferta_form(request.POST)
            if form.is_valid():
                o_monto = float(form.cleaned_data['o_monto'])
                max_bid = Oferta.objects.filter(id_subasta=product.subasta).aggregate(Max('o_monto'))['o_monto__max']
                if max_bid is None:
                    max_bid = 0.0
                if o_monto > max_bid:
                    Oferta.objects.create(
                        id_user=request.user,
                        id_subasta=product.subasta,
                        o_monto=o_monto
                    )
                else:
                     messages.error(request, 'La oferta debe ser mayor que la oferta máxima actual.')
                     return redirect('products', producto_id=producto_id)
        return redirect('products', producto_id=producto_id)
    
def close_bid(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    ofertas = Oferta.objects.filter(id_subasta=producto.subasta).order_by('-o_monto')
    subasta = Subasta.objects.get(pk=producto.subasta.pk)
    
    if ofertas.exists():
        oferta_ganadora = ofertas.first()
        ganador = oferta_ganadora.id_user
        subasta.s_estado = False
        # mover producto a tabla subastado
        Subastado.objects.create(
                        won_user=ganador,
                        id_subasta=producto.subasta,
                        id_producto=producto
                    )   
        subasta.save()       
        messages.success(request, f"Subasta cerrada. El ganador es: {ganador}")
    else:
        messages.error(request, "No hay ofertas en esta subasta.")
    return redirect('products', producto_id=producto_id)


def comentario(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST" and request.user.is_authenticated:   
        coment_form = Coment_form(request.POST) 
        if coment_form.is_valid():
                comment = Comentario(
                s_coment=request.POST["s_coment"],
                id_user=request.user,
                id_producto=producto
                )
                comment.save()
                messages.success(request, 'Comentario saved successfully!')
        else:
             print(coment_form.errors)  # errores de comentario     

    return redirect('products', producto_id=producto_id)   


def show_watchlist(request): 
    if request.user.is_authenticated:
        try:
             watchlist_items = Watchlist.objects.filter(user=request.user).values_list('w_producto', flat=True)
             productos = Producto.objects.filter(id__in=watchlist_items)
             subastado_product_ids = Subastado.objects.filter(id_producto__in=watchlist_items).values_list('id_producto', flat=True)
             productos_no_subastados = productos.exclude(id__in=Subquery(subastado_product_ids))
             subastado_won_user = Subastado.objects.filter(id_producto=OuterRef('pk')).values('won_user')[:1]
             productos_subastados = productos.filter(id__in=Subquery(subastado_product_ids)).annotate(won_user=Subquery(subastado_won_user))


             context = {
                    'productos_no_subastados': productos_no_subastados,
                    'productos_subastados': productos_subastados,
                    'MEDIA_URL': settings.MEDIA_URL,                     
                }
        except Watchlist.DoesNotExist:
                raise Http404("No tiene Watchlist o algun error al crearla")
        return render(request, 'auctions/show_watchlist.html', context)
    

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
