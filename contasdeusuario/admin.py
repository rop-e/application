from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario


class FormularioCriacaoUsuario(forms.ModelForm):
    """Formulário para criação de usuário"""
    senha1 = forms.CharField(
             label='Senha',
             widget=forms.PasswordInput)
    senha2 = forms.CharField(
             label='Confirmação de Senha',
             widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = (
            'nome',
            'sexo',
            'email',
            'dtnascimento',
            'cpf',
            'matricula',
        )

    def clean_password2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("Senhas não combinam!")
        return senha2

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["senha1"])
        if commit:
            usuario.save()
        return usuario


class FormularioAlteracaoUsuario(forms.ModelForm):
    """Formulário de alteração de policial"""
    senha = ReadOnlyPasswordHashField()

    class Meta:
        model = Usuario
        fields = (
            'nome',
            'sexo',
            'email',
            'dtnascimento',
            'cpf',
            'matricula',
            'is_active',
            'is_staff',
        )

    def clean_password(self):
        return self.initial["senha"]


class UsuarioAdmin(BaseUserAdmin):
    form = FormularioAlteracaoUsuario
    add_form = FormularioCriacaoUsuario

    list_display = (
        'matricula',
        'nome',
        'email',
        'is_staff'
    )
    list_filter = (
        'groups',
        'is_active'
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                    'matricula',
                    'nome',
                    'sexo',
                    'email',
                    'cpf',
                    'dtnascimento',
                    'senha1',
                    'senha2'
                ),
        }),
    )
    search_fields = (
        'matricula',
        'nome',
        'email'
    )
    ordering = ('nome',)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups'
            )
        else:
            perm_fields = (
                'is_active',
                'groups'
            )

        return [
            (None, {'fields': ('matricula', 'senha')}),
            ('Informações pessoais', {'fields': (
                    'nome',
                    'sexo',
                    'cpf',
                    'email',
                    'dtnascimento',
                )
            }),
            (('Permissões'), {'fields': perm_fields})
        ]


admin.site.register(Usuario, UsuarioAdmin)
