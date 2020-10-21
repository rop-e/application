import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from ropd.settings import (
    MEDIA_URL,
    PDF_ROOT
)


def link_callback(uri, rel):
    sUrl = settings.STATIC_URL
    sRoot = settings.STATIC_ROOT
    mUrl = settings.MEDIA_URL
    mRoot = settings.MEDIA_ROOT

    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri

    if not os.path.isfile(path):
        raise Exception('media URI must start with %s or %s' % (sUrl, mUrl))
    return path


def GerarPDF(template_path=str, context=dict, arquivo=str):
    template = get_template(template_path)
    html = template.render(context)

    pdf = open(PDF_ROOT + arquivo, "w+b")

    pisaStatus = pisa.CreatePDF(html, dest=pdf, link_callback=link_callback)

    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return MEDIA_URL + 'pdf/' + arquivo
