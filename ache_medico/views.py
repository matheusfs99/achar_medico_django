from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.core.mail import send_mail

# Create your views here.
def home(request):
    context = {}
    medicos = Medico.objects.all()
    busca_esp = request.GET.get('search-esp')
    if busca_esp:
        medicos = Medico.objects.filter(especialidade__icontains = busca_esp).order_by('especialidade')
    context['medicos'] = medicos
    print(medicos)
    return render(request, 'index.html', context)

def do_login_medico(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('pagina_medico/{}'.format(user.id))
    return render(request, 'login_medico.html')

def do_logout(request):
    logout(request)
    return redirect('login_medico')

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
def area_medico(request, id):
    context = {}
    medico = Medico.objects.get(id=id)
    formUser = UsersForms(request.POST or None)
    formMedico = MedicoForms(request.POST or None, request.FILES)
    formBio = BioForm(request.POST or None, instance=medico)
    context['medico'] = medico
    context['formMedico'] = formMedico
    context['formUser'] = formUser
    if medico.foto != '':
        foto = Medico.objects.filter(foto__exact=medico.foto)
        context['foto'] = foto
    if request.method == 'POST':
        if formBio.is_valid():
            formBio.save()
        return redirect('/pagina_medico/{}'.format(id))
    return render(request, 'area_medico.html', context)

@login_required
def edt_perfil(request, id):
    context = {}
    user = User.objects.get(id=id)
    medico = Medico.objects.get(id=id)
    formUser = UsersForms(request.POST or None, instance=user)
    formMedico = MedicoForms(request.POST or None, instance=medico)
    context['formMedico'] = formMedico
    context['formUser'] = formUser
    if request.method == 'POST':
        if all((formUser.is_valid(), formMedico.is_valid())):
            user = formUser.save()
            medico = formMedico.save(commit=False)
            medico.user = user
            medico.save()
            return redirect('logout')
    return render(request, 'editar_medico.html', context)

@login_required
def add_planos(request, id):
    context = {}
    medico = Medico.objects.get(id=id)
    formPlano = PlanosForm(request.POST or None, instance=medico)
    context['formPlano'] = formPlano
    if request.method == 'POST':
        if formPlano.is_valid():
            formPlano.save()
            return redirect('/pagina_medico/{}'.format(id))
    return render(request, 'add_plano_saude.html', context)


def perfil_medico_view(request, id):
    context = {}
    medico = Medico.objects.get(id=id)
    context['medico'] = medico
    if medico.foto != '':
        foto = Medico.objects.filter(foto__exact=medico.foto)
        context['foto'] = foto
    return render(request, 'perfil_medico_view.html', context)