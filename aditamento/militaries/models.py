from django.db import models
from aditamento.militaries.validators import validate_cpf


class Military(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    create_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'militar'
        verbose_name_plural = 'militares'

    def __str__(self):
        return self.name