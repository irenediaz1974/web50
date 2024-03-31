from django.urls import path

from . import views

app_name="wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path('search/', views.search, name='search'),
    path ("new/", views.new, name="new"),
    path('add/<str:title>/', views.add, name='add')
]
