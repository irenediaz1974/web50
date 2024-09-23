from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path('categories', views.categories, name='categories'),
    path("add_watchlist", views.add_watchlist, name="add_watchlist"), 
    path('add_subasta', views.add_subasta, name='add_subasta'),
    path("<int:producto_id>", views.products, name='products'),
    path("register", views.register, name="register")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)