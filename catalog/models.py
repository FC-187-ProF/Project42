from django.conf import settings
from django.db import models

class product(models.Model):
    name = models.CharField(max_length=2000, help_text="Наименование товара")
    height = models.FloatField(help_text="Ширина")
    length = models.FloatField(help_text="Длинна/диаметр")

    