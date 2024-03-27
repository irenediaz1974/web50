from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django.http import HttpResponse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # Crear clase markdown para usarla para convertir de markdown a html
    if util.get_entry(title):
        mark_cont=Markdown()
        return render(request, "encyclopedia/title.html", {
            "title": title,
            "title_cont": mark_cont.convert(util.get_entry(title))
            }) 
    else:
        error_message="no se que poner aqui"
        return render(request,"encyclopedia/404.html", {"error_message": error_message} )


def search(request):
    # check if the file name is in a search string
    if request.method == "GET":
     filenames= util.list_entries()
     search_string= request.GET.get('q').lower()
     found_entries=[]
     for filename in filenames:
            if (search_string == filename.lower()):
                mark_cont=Markdown()
                return render(request, "encyclopedia/title.html", {
                "title": search_string,
                "title_cont": mark_cont.convert(util.get_entry(search_string))
                })              
           
            elif (search_string) in filename.lower():
                found_entries.append(filename.lower())
                  
     if len(found_entries):
           return render(request, "encyclopedia/index.html", {
        "entries": found_entries
        })
    if len(found_entries)==0: 
        error_message ="Lo sentimos, no pudimos encontrar la página que estás buscando."
        return render(request,"encyclopedia/404.html", {"error_message": error_message} )


def new(request):
    if request.method == "GET":
       return render(request,"encyclopedia/new.html")
    elif request.method == "POST":
        
        save_data(request)
        return render(request,"encyclopedia/new.html")

def save_data(request):
    #Salvar los datos de entrada en un fichero.md
     title= request.GET.get('title').lower()
     if not util.get_entry(title):
        mark_cont=Markdown()
        mark_cont.convert(util.get_entry(title))       
     else: 
         error_message="El nombre del title ya existe"
         return render(request, "encyclopedia/404.html", {"error_message": error_message} )