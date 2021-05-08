from django.shortcuts import render
from markdown2 import Markdown
from . import util
from random import choice 


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def wiki(request, title): 
    markdowner = Markdown()
    return render(request, "encyclopedia/entry.html", {
        "content": markdowner.convert(util.get_entry(title)),
        "title":title
    })
def search(request): 
    title = request.POST['article']
    entries = util.list_entries()
    if title in entries:     
        markdowner = Markdown()
        return render(request, "encyclopedia/entry.html", {
            "content": markdowner.convert(util.get_entry(title)),
            "title": title
        })
    else:
        contained = []
        for entry in entries:
            if title in entry: 
                contained.append(entry)
        return render(request, "encyclopedia/entries.html", {
                "entries": contained,
                "title": title
         })
def createpage(request): 
    return render(request, "encyclopedia/createpage.html", {
        "entries": util.list_entries()
      })
def new_page(request):
    title = request.POST['title']
    entries = util.list_entries()
    if title in entries: 
        return render(request, "encyclopedia/error.html", {
            "title": title
        })
    entry = request.POST['entry']
    util.save_entry(title, entry)
    return wiki(request, title)
def new_edit(request):
    markdowner = Markdown()
    title = request.POST['title']
    content = request.POST['content']
    return render(request, "encyclopedia/editpage.html", {
        "title": title,
        "content": util.get_entry(title)
    })
def submit_edit(request):
    marked_content = request.POST['entry']
    title = request.POST['title']
    util.save_entry(title, marked_content)
    markdowner = Markdown()
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdowner.convert(util.get_entry(title))
    })
def random(request): 
    list = util.list_entries()
    return wiki(request, choice(list))


