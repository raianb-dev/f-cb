# views.py
from django.shortcuts import render, redirect
import requests

def painel(request):
    if not request.session.get('login'):
        return redirect('login') 
    
    dropdown_options = [
        {'value': 'DEMO', 'label': 'DEMO', 'selected': True},
        {'value': 'BRL', 'label': 'BRL', 'selected': False},
        {'value': 'BTC', 'label': 'BTC', 'selected': False},
    ]
    email = ""
    password = ""
    currency = "none"
    bet_min = None
    status_code = None
    betnofloat = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        currency = request.POST.get('dropdown')
        bet_min = request.POST.get('bet_min')
        print(email, password, currency, bet_min)

        # Convertendo bet_min para float (número decimal)
        try:
            bet_min = float(bet_min)
        except ValueError:
            bet_min = None
        
        if bet_min is not None:
            data = {
                "username": email,
                "password": password,
                "bet": int(bet_min),
                "currency": currency,
            }
            req = requests.post(url="http://vps54611.publiccloud.com.br:5000/double/start", json=data)
            status_code = req.status_code
            print(status_code)
        else:
            print("Valor de aposta inválido:", bet_min)

    return render(request, 'painel.html', {
        'dropdown_options': dropdown_options,
        'email': email,
        'password': password,
        'bet_min': bet_min,
        'currency': currency,
        'status_code': status_code
    })
