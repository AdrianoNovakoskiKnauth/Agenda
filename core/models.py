from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(verbose_name='Evento', max_length=100)               #Campo caracter com maximo de 100
    descricao = models.TextField(verbose_name='Descrição do evento', blank=True, null=True)   #Campo texto que pode ficar embranco e nulo
    data_evento = models.DateTimeField(verbose_name='Data do evento')                    #Campo data que não pode ficar em branco
    date_criacao = models.DateTimeField(verbose_name='Data de criação', auto_now=True)      #Data criação que preeche automatico        #Obs no datE_criacao
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Usuário')         #Atribui o evento a um usuáro

    class Meta:
        db_table = 'evento'                                 #definir o nome do modúlo

    def __str__(self):
        return self.titulo                                  #Informa o nome de cada agendamento pelo tilulo dele

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_evento_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False