from django.shortcuts import render


def index(request): 
 
    return render(request,'index.html')

def administrador(request):

    agenda = {
        1:'30/07/3030',
        2:'23/9/2093',
        3: '23/44/222'
    }

    dados = {
        'agendamento' : agenda
    }
    return render (request, 'administrador.html', dados)
    
def usuario(request):
    return render (request, 'usuario.html')