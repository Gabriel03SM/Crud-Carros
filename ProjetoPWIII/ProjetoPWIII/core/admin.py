from django.contrib import admin
from.models import Carro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'marca', 'cor', 'valor')
    list_filter = ['nome']
