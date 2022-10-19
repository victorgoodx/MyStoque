from crypt import methods
import email
from http.client import REQUEST_URI_TOO_LONG, HTTPResponse
from re import search
from ssl import _PasswordType, AlertDescription
from django.shortcuts import render, redirect
from app.forms import ProdutosForm
from app.models import Produtos
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="/auth/login/")
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Produtos.objects.filter(produto__icontains=search)
    else:
        data['db'] = Produtos.objects.all()
    return render(request, 'index.html', data)

@login_required(login_url="/auth/login/")
def form(request):
    data = {}
    data['form'] = ProdutosForm()
    return render(request, 'form.html', data)

@login_required(login_url="/auth/login/")
def create(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

@login_required(login_url="/auth/login/")
def edit(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'form.html', data)

@login_required(login_url="/auth/login/")
def update(request, pk):
    data = {}
    data['db'] = Produtos.objects.get(pk=pk)
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

@login_required(login_url="/auth/login/")
def delete(request, pk):
    db = Produtos.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    else:
        username = request.POST .get("username")
        email = request.POSt.get("email")
        senha = request.POSt.get("senha")

        user = User.objects.filter(username=username).first()

        if user:
            return HTTPResponse("já existe um usúario com esse username")

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return HTTPResponse("Usúario cadastrado com sucesso")

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return AlertDescription('Email ou Senha inválidos')

    