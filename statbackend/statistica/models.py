from django.db import models

# Create your models here.


class Info(models.Model):
    date = models.DateField()
    views = models.IntegerField(blank=True, default=0)
    clicks = models.IntegerField(blank=True, default=0)
    cost = models.DecimalField(max_digits=12, decimal_places=2, blank=True, default=0)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Стастистики'