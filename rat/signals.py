from .models import RAT
from django.db.models.signals import post_save
from utils.pycrypto import encrypt


def save_rat(sender, instance, **kwargs):
    if instance.status_previa == False:
        message = """ID DA GUARNIÇÃO: {}
MATRÍCULA DO COMANDANTE DA GUARNIÇÃO: {}
ID DA RAT: {}
DATA CRIAÇÃO DA RAT: {}""".format(
            instance.guarnicao.id,
            instance.guarnicao.comandante.id,
            instance.id,
            instance.datacriacao)
        
        RAT.objects.filter(id=instance.id).update(hash=encrypt(message))

post_save.connect(save_rat, sender=RAT)
