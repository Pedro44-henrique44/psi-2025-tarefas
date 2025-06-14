from django.urls import path
from . import views
urlpatterns = [
    path('', views.inicio, name="inicio")
]


#ao mudar ou adicionar uma página(html), mude: views."{mude aqui}", name="{mude aqui}". isso muda as URLs.