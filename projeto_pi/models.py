from django.db import models
#from datetime import datetime

class Funcionario(models.Model):
    id_func = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_FUNC'),
    nome = models.CharField(max_length=50),
    setor = models.CharField(max_length=10, choices=[('Compras','COMPRAS'), ('Administrativo', 'ADM'), ('Almoxarifado','ALMOX')]),
    chefe_setor = models.BooleanField(default=False),
    data_admissao = models.DateField(),
    email = models.CharField(max_length=50)

class Ferias(models.Model):
    id_ferias = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_FERIAS'),
    id_func = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    data_inicio = models.DateField(verbose_name='data de início'),
    data_fim = models.DateField(verbose_name='data de fim'),
    periodo =  models.IntegerField(choices=[('30 dias', 30), ('20 dias', 20), ('15 dias', 15)], default=30),
    status = models.CharField(choices=[('DEFERIDO','Deferido'), ('INDEFERIDO', 'Indeferido')],max_length=10)
            
class Agenda(models.Model):
    id_agenda = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID_AGENDA'),
    id_func = models.ForeignKey('Funcionario', on_delete=models.CASCADE),
    data_agenda = models.DateField(verbose_name='data do agendamento'),
    hora_agenda = models.DateTimeField(verbose_name='horário do agendamento'),
    pauta_agenda = models.CharField(max_length=500)


