from django.urls import path
from galeria.views import index, imagem #adicionais

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    #path('adicionais/', adicionais, name='adicionais')
]
