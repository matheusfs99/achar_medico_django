from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('logout', do_logout, name='logout'),
    path('login_medico', do_login_medico, name='login_medico'),
    path('cadastro_medico', cadastro_medico, name='cadastro_medico'),
    path('pagina_medico/<int:id>', area_medico, name='area_medico'),
]