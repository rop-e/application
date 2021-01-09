from .models import Ocorrencia
from django.db.models.signals import post_save
from utils.pycrypto import encrypt
from django.conf import settings


def save_ocorrencia(sender, instance, **kwargs):
    if instance.status_previa == False:
        message = """ID DA GUARNIÇÃO: {}
MATRÍCULA DO COMANDANTE DA GUARNIÇÃO: {}
ID DA OCORRÊNCIA: {}
DATA CRIAÇÃO DA OCORRÊNCIA: {}""".format(
            instance.guarnicao.id,
            instance.guarnicao.comandante.id,
            instance.id,
            instance.datacriacao)
        
        Ocorrencia.objects.filter(id=instance.id).update(hash=encrypt(settings.SENHA_HASH, message))

post_save.connect(save_ocorrencia, sender=Ocorrencia)
