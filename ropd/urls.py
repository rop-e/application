from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    path,
    include
)

from contasdeusuario.views import CustomAuthToken

BASEURL = 'api/v0/'

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),

    # utils
    path(
        BASEURL+'utils/',
        include('utils.urls')),

    # painel administrativo
    path(
        '',
        include('dashboard.urls')),

    # autenticacao de usuario para o dashboard
    path('contas/', include('dashboard.auth.urls')),

    path(
        BASEURL+'policial/',
        include('policial.urls')),
    path(
        BASEURL+'rat/',
        include('rat.urls')),
    path(
        BASEURL+'opo/',
        include('opo.urls')),
    path(
        BASEURL+'pessoa/',
        include('pessoa.urls')),
    path(
        BASEURL+'veiculo/',
        include('veiculo.urls')),
    path(
        BASEURL+'batalhao/',
        include('batalhao.urls')),
    path(
        BASEURL+'endereco/',
        include('endereco.urls')),
    path(
        BASEURL+'guarnicao/',
        include('guarnicao.urls')),
    path(
        BASEURL+'envolvido/',
        include('envolvido.urls')),
    path(
        BASEURL+'viatura/',
        include('viatura.urls')),
    path(
        BASEURL+'policialviatura/',
        include('policialviatura.urls')),
    path(
        BASEURL+'ocorrencia/',
        include('ocorrencia.urls')),
    path(
        BASEURL+'anexo/',
        include('anexo.urls')),
    path(
        BASEURL+'observacao/',
        include('observacao.urls')),
    path(
        BASEURL+'localrecebedor/',
        include('localrecebedor.urls')),
    path(
        BASEURL+'procedimentoocorrencia/',
        include('procedimentoocorrencia.urls')),
    path(
        BASEURL+'acessoriosocorrencia/',
        include('acessoriosocorrencia.urls')),

    # path(BASEURL + 'api-token/', views.obtain_auth_token, name='api-token'),
    path(BASEURL + 'api-token/', CustomAuthToken.as_view())

]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)  # fotos
