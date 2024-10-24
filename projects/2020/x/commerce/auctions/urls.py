from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('categories', views.categories, name='categories'),
    path('show_watchlist', views.show_watchlist, name='show_watchlist'),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"), 
    path('add_subasta', views.add_subasta, name='add_subasta'),
    path('place_bid/<int:producto_id>', views.place_bid, name='place_bid'),
    path('close_bid/<int:producto_id>', views.close_bid, name='close_bid'),
    path("<int:producto_id>", views.products, name='products'),
    path('add_watchlist/<int:producto_id>/', views.add_watchlist, name='add_watchlist'),
    path('remove_watchlist/<int:producto_id>/', views.remove_watchlist, name='remove_watchlist'),
    path("register", views.register, name="register"),
    path("comentario/<int:producto_id>/", views.comentario, name="comentario")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)