from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django.http import HttpResponse
from django.http import HttpResponseNotAllowed
from django.core.files.storage import default_storage
import errno


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
        error_message="Error al generar el fichero"
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
        title_mkup= request.POST["title_text"]
        text_mkup=request.POST["texto"]
        error_message= save_data(request, title_mkup.lower(), text_mkup) 
        if (error_message)=="":
            mark_cont=Markdown()
            return render(request, "encyclopedia/title.html", {
            "title": title_mkup.lower(),
            "title_cont": mark_cont.convert(util.get_entry(title_mkup.lower()))
            }) 
        else:
            return render(request, "encyclopedia/404.html", {"error_message": error_message} ) 
    else:
        return HttpResponseNotAllowed(['GET', 'POST']) 

def save_data(request, title_mkup, text_mkup):
    #Salvar los datos de entrada en un fichero.md
     
     if  util.get_entry(title_mkup) == None:
        try:
             file= default_storage.open(f"entries/{title_mkup}.md", 'w') 
             file.write(f"# {title_mkup.upper()}\n\n{text_mkup}")
             file.close()
             error_message=""
             return (error_message)
        except PermissionError:
            error_message= "You do not have permission to write to this file." + title_mkup
        except OSError as e:
             if e.errno == errno.ENOSPC:
                 error_message="The disk is full."
             else:
                 error_message="An OS error occurred."
              
     else: 
         error_message= "Ya existe un documento con el mismo nombre" + title_mkup   
         return (error_message)