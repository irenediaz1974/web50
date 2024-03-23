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
        return render(request,"encyclopedia/404.html")


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
        return render(request,"encyclopedia/404.html")


def new(request):
       return render(request,"encyclopedia/new.html")
