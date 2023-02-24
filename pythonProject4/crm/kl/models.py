from django.db import models

class listofcompanies(models.Model):
    name = models.CharField('Назва', max_length=255)
    city = models.CharField('Місто', max_length=255)
    industry = models.CharField('Галузь', max_length=255)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Компанія'
        verbose_name_plural = 'Компанії'