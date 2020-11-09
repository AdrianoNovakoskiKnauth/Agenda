from typing import Tuple

from django.contrib import admin
from core.models import Evento


# Register your models here.
class EventoAdmin(admin.ModelAdmin):                                    #Class para difiniar os campos que iram aparecer
     list_display = ('id','titulo', 'data_evento', 'date_criacao', 'usuario',)           #Obs no datE_criacao
     list_filter = ('usuario', 'data_evento',)

admin.site.register(Evento, EventoAdmin)
