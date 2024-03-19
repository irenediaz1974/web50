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
     for filename in filenames:
            # if the string is the same name of *.md file
            if (request("q").lower() == filename.lower()):
                mark_cont=Markdown()
                return render(request, "encyclopedia/title.html", {
                "title": request("q").capitalize(),
                "title_cont": mark_cont.convert(util.get_entry(request("q").capitalize()))
            })              
           # elif(request("q").lower() in filename.lower()):   
            else:
                return render(request,"encyclopedia/404.html")

