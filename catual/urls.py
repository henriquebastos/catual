from django.conf.urls import include, url
from django.contrib import admin

from catual.core.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^olimpo/', include('catual.olimpo.urls', namespace='olimpo')),
    url(r'^admin/', include(admin.site.urls)),
]
