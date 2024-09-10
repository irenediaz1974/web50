from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("addProducto", views.add_producto, name="addProducto"), 
    path('add_subasta', views.add_subasta, name='add_subasta'),
    path('categories', views.categories, name='categories'),
    path("register", views.register, name="register")
]
