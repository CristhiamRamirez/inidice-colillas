from dataclasses import field
from statistics import median_grouped, mode
from django.db import models

NOMINAS = (
    (1,"Semanal"),
    (2,"Quincenal")
)


class Period(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(max_length=9,null=False)
    number = models.SmallIntegerField(null=False)
    year = models.SmallIntegerField(null=False)
    start = models.DateField(null=False)
    end = models.DateField(null=False)


class Boucher(models.Model):
    id = models.IntegerField(primary_key=True)
    period = models.ForeignKey(Period, null=False, on_delete=models.CASCADE)
    payroll_type = models.SmallIntegerField(null=False, choices=NOMINAS)
    package = models.SmallIntegerField(null=False)
    index = models.SmallIntegerField(null=False)
    key = models.TextField(null=False, blank=False)
    employee = models.IntegerField(null=False)
