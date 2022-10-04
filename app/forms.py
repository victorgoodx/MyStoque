from dataclasses import fields
from django.forms import ModelForm
from app.models import Produtos

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['produto', 'codigo', 'ano_validade', 'quantidade']