from django.conf.urls import url
from catual.olimpo.views import ocorrencias, painel, eventos, login
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', painel, name='painel'),
    url(r'^ocorrencias/$', ocorrencias, name='ocorrencias'),
    url(r'^eventos/$', eventos, name='eventos'),
    #url(r'^entrar/$', login, {'template_name': 'olimpo/login.html'}, name='login'),
    url(r'^sair/$', logout, {'next_page': 'home'}, name='logout'),
    url(r'^login/$', login,  name='login'),
]