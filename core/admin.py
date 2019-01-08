from django.contrib import admin
from .models import *


class RevistaInlineAdmin(admin.TabularInline):
    model = Revista
    extra = 0

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class ColecaoAdmin(admin.ModelAdmin):
    inlines = [RevistaInlineAdmin]
    list_display = ('nome',)
    search_fields = ('nome',)


class AmigoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'nome_mae','telefone',)
    ordering = ('nome',)
    list_filter = ('grupo_amigo',)
    search_fields = ('nome',)


class CaixaAdmin(admin.ModelAdmin):

    list_display = ('numero', 'etiqueta','cor',)
    ordering = ('cor',)
    list_filter = ('cor',)
    search_fields = ('cor', 'numero')


class RevistaAdmin(admin.ModelAdmin):

    list_display = ('numero_edicao', 'ano')
    ordering = ('ano',)
    list_filter = ('ano',)
    search_fields = ('ano',)


class EmprestimoAdmin(admin.ModelAdmin):

    list_display = ('data_emprestimo', 'data_devolucao','nome_do_amigo','numero_da_revista')
    ordering = ('data_emprestimo',)
    list_filter = ('data_emprestimo',)
    search_fields = ('nome_do_amigo','numero_da_revista')


admin.site.register(Colecao, ColecaoAdmin)
admin.site.register(Amigo, AmigoAdmin)
admin.site.register(Caixa, CaixaAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
admin.site.register(Revista,RevistaAdmin)



#default:"Administração do Django"
admin.site.site_header='Painel de Controle'

#default:"Administração do Site"
admin.site.index_title=''

#default:"Site de Administração do Django"
admin.site.site_title='Questão 04'
