from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Produto
from .forms import ProdutoForm


def produto(request, id):
    item = Produto.objects.get(pk=id)
    return render(request, 'produto.html', {'item': item})

def lista_produtos(request):
    items = Produto.objects.all()
    return render(request, 'lista_produtos.html', {'items': items})

@login_required
def novo_produto(request):
    form = ProdutoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produto_form.html', {'form': form})

@login_required
def update_produto(request, id):
    item = Produto.objects.get(pk=id)
    form = ProdutoForm(
        request.POST,
        request.FILES,
        instance=item
    )

    if form.is_valid():
        form.save()
        return redirect('lista_produtos')

    return render(request, 'produto_form.html', {'form': form})

@login_required
def delete_produto(request, id):
    item = Produto.objects.get(pk=id)

    if request.method == 'POST':
        item.delete()
        return redirect('lista_produtos')

    return render(request, 'delete_produto.html', {'item': item})
