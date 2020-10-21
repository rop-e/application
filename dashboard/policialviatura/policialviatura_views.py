from policialviatura.models import PolicialViatura


def listar_policiais_na_viatura(id):
    pm = PolicialViatura.objects.all().filter(guarnicao_id=id)
    return pm
