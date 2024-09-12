# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),  # aggiungi questa riga per la pagina di default
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),
]
