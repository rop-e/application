from django.contrib import admin
from .models import (
    Pessoa,
    PessoaEndereco
)

admin.site.register(Pessoa)
admin.site.register(PessoaEndereco)
