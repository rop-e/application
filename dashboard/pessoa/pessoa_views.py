from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from pessoa.models import Pessoa


@login_required
def buscar_pessoa(request):
    if request.is_ajax():
        pessoas = Pessoa.objects.filter(
            nome__istartswith=request.GET.get("term", None))
        results = []

        for pessoa in pessoas:
            pessoas_objeto = {
                "id": pessoa.id,
                "nome": pessoa.nome,
                "sexo": pessoa.sexo,
                "datanascimento": pessoa.datanascimento,
                "mae": pessoa.mae,
                "apelido": pessoa.apelido,
                "cpf": pessoa.cpf,
                "rg": pessoa.rg,
                "cnh": pessoa.cnh
            }
            results.append(pessoas_objeto)

        return JsonResponse(results, safe=False)
