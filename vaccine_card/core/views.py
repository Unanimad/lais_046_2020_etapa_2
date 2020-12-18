from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse


def login(request):
    template_name = 'panel/login.html'

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)

                if user.is_staff:
                    return HttpResponseRedirect(reverse('panel:index'))
                else:
                    return HttpResponseRedirect(reverse('panel:login'))

            else:
                messages.error(request, 'Conta inativa.')
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, template_name)


def logout(request):
    auth_logout(request)

    return redirect('/panel/login')


@login_required
def index(request):
    template_name = 'panel/index.html'

    context = {
        'head_title': 'Painel',
    }

    return render(request, template_name, context)


def handler404(request):
    return redirect('/login')
