from django.shortcuts import render, redirect
from login.models import Usuario

def index(request):
    if request.method == 'POST':
        login = request.POST.get('login')
        senha = request.POST.get('senha')
        
        # Verifica se o login e a senha correspondem a um usuário na base de dados
        usuario = Usuario.objects.filter(login=login, senha=senha).first()
        
        if usuario:
            # Armazena o login na sessão
            request.session['login'] = login
            return redirect('painel')
    
    return render(request, 'login.html')
