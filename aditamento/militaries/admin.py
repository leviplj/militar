from django.contrib import admin
from aditamento.militaries.models import Military

class MilitaryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf')
    search_fields = ('name', 'cpf')

admin.site.register(Military, MilitaryModelAdmin)

