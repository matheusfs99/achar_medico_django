from django.urls import path
from .views import *

urlpatterns = [
    path('', do_login, name='login'),
    path('logout', do_logout, name='logout'),
    path('cadastro', cadastro_user, name='cadastro_user'),
    path('menu/<int:id>', home, name='menu'),
    path('login_medico', do_login_medico, name='login_medico'),
    path('cadastro_medico', cadastro_medico, name='cadastro_medico'),
    path('pagina_medico/<int:id>', area_medico, name='area_medico'),
]