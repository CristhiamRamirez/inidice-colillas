from dataclasses import field
from statistics import median_grouped, mode
from django.db import models

NOMINAS = {"Semanal":1, "Quincenal":2}


class Periodos(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.TextField(max_length=9,null=False)
    numero = models.SmallIntegerField(null=False)
    año = models.SmallIntegerField(null=False)
    inicio = models.DateField(null=False)
    fin = models.DateField(null=False)


class Boleta(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_nomina = models.SmallIntegerField(null=False, choices=NOMINAS)
    periodo = models.SmallIntegerField(null=False)
    paquete_numero = models.SmallIntegerField(null=False)
    empleado = models.IntegerField(null=False)
