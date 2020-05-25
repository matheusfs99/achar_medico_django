from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

# Create your views here.

def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('menu/{}'.format(user.id))
    return render(request, 'index.html')

def do_logout(request):
    logout(request)
    return redirect('login')

def do_login_medico(request):
    if request.method == 'POST':
        medico = authenticate(username=request.POST['username'], password=request.POST['password'])
        if medico is not None:
            login(request, medico)
            return redirect('pagina_medico/{}'.format(medico.id))
    return render(request, 'login_medico.html')

def cadastro_user(request):
    form = UsersForms(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            '''
            send_mail(
                'Ache seu Médico - Cadastro Efetuado com Sucesso!',
                'Olá ex!\nSeu cadastro no Ache seu Médico foi efetuado com sucesso. Obrigado por utilizar nosso site.\nEsperamos que você consiga encontrar o médico perfeito para o seu caso.\n\nSeu nome de usuário cadastrado é: ex\n\nEste é um email eletrônico. Não responda este email.',
                'mensagem@acheseumedico.com.br',
                ['matheusfarias009@hotmail.com'],
                fail_silently=False,
            )
            '''
            form.save()
            return redirect('login')
    return render(request, 'cadastro_user.html', context)

def cadastro_medico(request):
    formUser = UsersForms(request.POST or None)
    formMedico = MedicoForms(request.POST or None, request.FILES)
    context = {'formUser': formUser, 'formMedico': formMedico}
    if request.method == 'POST':
        if all((formUser.is_valid(), formMedico.is_valid())):
            user = formUser.save()
            medico = formMedico.save(commit=False)
            medico.user = user
            medico.save()
            return redirect('login_medico')
    return render(request, 'cadastro_medico.html', context)

@login_required
def home(request, id):
    return render(request, 'menu.html')

@login_required
def area_medico(request, id):
    context = {}
    medico = Medico.objects.get(id=id)
    context['medico'] = medico
    return render(request, 'area_medico.html', context)

