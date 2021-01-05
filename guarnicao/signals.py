from .models import Guarnicao
from policialviatura.models import PolicialViatura
from django.db.models.signals import post_save

def save_guarnicao(sender, instance, **kwargs):
    if instance.datafechamento is not None:
        PolicialViatura.objects.filter(guarnicao=instance.pk).update(ativo=False)

post_save.connect(save_guarnicao, sender=Guarnicao)
