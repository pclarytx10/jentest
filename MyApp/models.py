from django.db import models

# Create your models here.


class Coin(models.Model):
    coin_name = models.CharField(max_length=50)
    api_id = models.CharField(max_length=250, blank=True)
    coin_symbol = models.CharField(max_length=10, blank=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ('coin_name',)

    def __str__(self) -> str:
        return self.coin_name
