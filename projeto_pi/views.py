from django.shortcuts import render 
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from . import models
import datetime

def index(request):
    return render(request, 'index.html')

def administrador(request):
    agendamentos = models.Agenda.objects.all()
    dados = {
        'agendamentos': agendamentos
    }
    return render(request, 'administrador.html', dados)
    
def usuario(request):
    return render(request, 'usuario.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        print(f'email: {email}')
        print(f'senha: {senha}')
        
        if models.Funcionario.objects.filter(email=email).exists:
            f = models.Funcionario.objects.filter(email=email).get()
            print(f'passou pelo f: {f}, senha: [{senha}], f.senha: [{f.senha}], {f.senha == senha}')
            if (not f) or (f.senha != senha):
                print('senha inválida')
                return render(request, 'index.html', {'erros': 
                    ['email ou senha inválidos']
                })
            elif f.chefe_setor:
                print('chefe')
                return administrador(request)
            else:
                print('usuario')
                return usuario(request)
        else:
            print('ERRO, não entrou no IF')
