from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('categories', views.categories, name='categories'),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"), 
    path('add_subasta', views.add_subasta, name='add_subasta'),
    path("register", views.register, name="register")
]
