from django.db import models
from games.models import Game


class OriginPrice(models.Model):
    """Модель, представляющая информацию о цене игры в различных магазинах или источниках."""
    origin_name = models.CharField(max_length=255, verbose_name='Название источника цены')
    buy_link = models.URLField(verbose_name='Ссылка для покупки')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    game = models.ForeignKey(Game, related_name='prices', on_delete=models.CASCADE, verbose_name='Игра')

    class Meta:
        db_table = 'origin_prices'

    def __str__(self):
        return f'{self.origin_name}: {self.price}'


class Pricing(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    game = models.ForeignKey(Game, related_name='pricing', on_delete=models.CASCADE, verbose_name='Игра')

    class Meta:
        db_table = 'pricing'

    def __str__(self):
        return f'Цена для игры: {self.game.title} - {self.price}'
