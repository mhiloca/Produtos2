from django.urls import path

from .views import produto, lista_produtos, novo_produto, update_produto, delete_produto

urlpatterns = [
    path('<int:id>/', produto, name='produto'),
    path('lista/', lista_produtos, name='lista_produtos'),
    path('novo/', novo_produto, name='novo_produto'),
    path('update/<int:id>/', update_produto, name='update_produto'),
    path('delete/<int:id>/', delete_produto, name='delete_produto'),
]