from django.shortcuts import render
from perfil.models import Conta,Categoria

def novo_valor(request):
    if request.method == 'GET':
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(request, 'novo_valor.html', {'contas': contas, 'categorias': categorias})
    elif request.method == 'POST':
        valor = request.POST.get('valor'),
        categoria = request.POST.get('categoria'),
        descricao = request.POST.get('descricao'),
        data = request.POST.get('data'),
        conta = request.POST.get('conta'),
        tipo = request.POST.get('tipo')
        
        valores = Valores(
            valor = valor,
            categoria = categoria,
            descricao = descricao,
            data = data,
            conta = conta,
            tipo = tipo
        )
        
        valores.save()
    
