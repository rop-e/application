from django import template
from django.contrib.auth.models import Group
from guarnicao.models import Guarnicao
from policialviatura.models import PolicialViatura

register = template.Library()


@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] !=
                                      field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url


@register.filter(name='guarnicao_ativa')
def guarnicao_ativa(request):
    guarnicao = Guarnicao.objects.filter(comandante_id=request.user.policial.id, datafechamento=None).last()
    return True if guarnicao else False


@register.filter(name='policialviatura_verifica')
def policialviatura_verifica(request):
    policialviatura = PolicialViatura.objects.filter(
        policial=request.user.policial.id, ativo=True).last()
    return True if policialviatura else False


@register.filter(name='policialviatura_comandante_guarnicao')
def policialviatura_comandante_guarnicao(request):
    try:
        policialviatura = PolicialViatura.objects.get(policial=request.user.policial.id, ativo=True)

        return policialviatura.guarnicao.comandante
    except Exception:
        pass


@register.filter(name='guarnicao_status')
def guarnicao_status(request):
    try:
        guarnicao = Guarnicao.objects.get(comandante_id=request.user.policial.id, datafechamento=None)

        return guarnicao.ativo
    except Exception:
        pass


@register.filter(name='id_guarnicao_ativa')
def id_guarnicao_ativa(request):
    try:
        guarnicao = Guarnicao.objects.get(comandante_id=request.user.policial.id, datafechamento=None)

        return guarnicao.id
    except Exception:
        pass


@register.filter(name='has_group')
def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
