from django.shortcuts import render
from markdown2 import Markdown
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    # Crear clase markdown para usarla para convertir de markdown a html
    mark_cont=Markdown()
    return render(request, "encyclopedia/title.html", {
         "title": title,
         "title_cont": mark_cont.convert(util.get_entry(title))
    }) 
