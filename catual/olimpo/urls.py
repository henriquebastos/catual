from django.conf.urls import url
from catual.olimpo.views import ocorrencias, painel, eventos
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', painel, name='painel'),
    url(r'^ocorrencias/$', ocorrencias, name='ocorrencias'),
    url(r'^eventos/$', eventos, name='eventos'),
    url(r'^entrar/$', login, {'template_name': 'olimpo/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'home'}, name='logout'),
]