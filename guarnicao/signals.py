from .models import Guarnicao
from policialviatura.models import PolicialViatura
from django.db.models.signals import post_save
from utils.pycrypto import encrypt, decrypt


def save_guarnicao(sender, instance, **kwargs):
    if instance.datafechamento is not None:
        PolicialViatura.objects.filter(guarnicao=instance.pk).update(ativo=False)
        message = """TIPO DE SERVIÇO: {} - ({})
MODALIDADE DE POLICIAMENTO: {} - ({})
COMPANHIA: {} - ({})
MATRÍCULA DO COMANDANTE DA GUARNIÇÃO: {} - ({})
MUNICÍPIO ATUANTE: {} - ({})
COORDENADOR DE ÁREA: {} - ({})
DATA DE ABERTURA DA GUARNIÇÃO: {}
DATA DE FECHAMENTO DA GUARNIÇÃO: {}""".format(
            instance.tiposervico.id, instance.tiposervico,
            instance.modalidadepoliciamento.id, instance.modalidadepoliciamento,
            instance.companhia.id, instance.companhia,
            instance.comandante.id, instance.comandante,
            instance.municipio.codigo_ibge, instance.municipio,
            instance.coordenadordearea.id, instance.coordenadordearea,
            instance.dataabertura,
            instance.datafechamento)

        Guarnicao.objects.filter(id=instance.id).update(hash=encrypt(message))


post_save.connect(save_guarnicao, sender=Guarnicao)
