from re import search
from django.shortcuts import render, redirect
from app.forms import ProdutosForm
from app.models import Produtos

# Create your views here.
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produtos.objects.filter(produto__icontains=search)
    else:
        data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = ProdutosForm()
    return render(request, 'form.html', data)

def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')
