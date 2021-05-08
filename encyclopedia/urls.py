from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name = "wiki"),
    path("search",views.search, name = "search"),
    path("createpage", views.createpage, name = "createpage"),
    path("wiki/", views.new_page, name = "newpage"),
    path("edit/", views.new_edit, name = "newedit"),
    path("edited/", views.submit_edit, name = "edit"),
    path("random/", views.random, name = "random")
    
]
