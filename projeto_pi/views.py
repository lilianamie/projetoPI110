from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from . import models
import datetime

def index(request):

    id_func = request.session.get('id_funcionario_logado')
    print(f'id_func:{id_func}')
    if not id_func:
        return render(request, 'index.html')
    else:
        funcionario_logado = models.Funcionario.objects.filter(id_func=id_func).get()
        print(f'funcionario_logado ={funcionario_logado}')
        if not funcionario_logado:
            return render(request, 'index.html')
        elif funcionario_logado.chefe_setor:
            return administrador(request)
        else:
            return usuario(request)

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
                return render(request, 'index.html', {'erros': ['email ou senha inválidos']})
            else:
                print(f'id_func = {f.id_func}')
                request.session['id_funcionario_logado'] = f.id_func
                return redirect('index')

        else:
            return render(request, 'index.html', {'erros': ['email ou senha inválidos']})


def administrador(request):
    agendamentos = models.Agenda.objects.all()
    ferias_agendadas = models.Ferias.objects.all()

    print(f'lista avisos:{agendamentos}')
    print(f'lista ferias:{ferias_agendadas}')

    dados= {
        'agendamentos': agendamentos,
        'ferias_agendadas': ferias_agendadas
    }
    return render(request, 'administrador.html', dados)
    
def usuario(request):
    agendamentos = models.Agenda.objects.all()
    ferias_agendadas = models.Ferias.objects.all()

    print(f'lista avisos:{agendamentos}')
    print(f'lista ferias:{ferias_agendadas}')

    dados = {
        'agendamentos': agendamentos,
        'ferias_agendadas': ferias_agendadas
    }
    return render(request, 'usuario.html', dados)

def solicitar_ferias(request):
    print('Entrou no metodo Solicitar ferias')
    id_func = request.session.get('id_funcionario_logado')
    funcionario_logado = models.Funcionario.objects.filter(id_func=id_func).get()
    if request.method == 'POST':
        periodo = int(request.POST['periodo'])
        data_inicio = datetime.date.fromisoformat(request.POST['data_inicio'])
        data_fim = data_inicio + datetime.timedelta(days=periodo)
        status = 'Pendente'
        print(f'Periodo = {periodo}, data_inicio = {data_inicio}, data_fim = {data_fim}, status = {status}')
        f = models.Ferias(funcionario=funcionario_logado, data_inicio=data_inicio, data_fim=data_fim, periodo=periodo, status=status)
        f.save()
        return redirect('usuario')


def logout(request):
    del request.session['id_funcionario_logado']
    return redirect('index')
