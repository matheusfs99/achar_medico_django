from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout', do_logout, name='logout'),
    path('login_medico', do_login_medico, name='login_medico'),
    path('cadastro_medico', cadastro_medico, name='cadastro_medico'),
    path('pagina_medico/<int:id>', area_medico, name='area_medico'),
    path('editar_perfil/<int:id>', edt_perfil, name='edt_perfil'),
    path('add_planos_saude/<int:id>', add_planos, name='add_planos')
]