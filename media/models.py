from django.db import models
from games.models import Game


class MediaLink(models.Model):
    """Модель для хранения ссылок на медиа-контент игры."""
    MEDIA_TYPE_CHOICES = [
        ('cover_image', 'Обложка'),
        ('background_video', 'Фоновое видео'),
        ('screenshot', 'Скриншот'),
        ('trailer', 'Трейлер'),
        ('other_video', 'Другое видео'),
    ]

    game = models.ForeignKey(Game, related_name='media_links', on_delete=models.CASCADE, verbose_name='Игра')
    media_type = models.CharField(max_length=20, choices=MEDIA_TYPE_CHOICES, verbose_name='Тип медиа')
    url = models.URLField(verbose_name='URL медиа')

    class Meta:
        db_table = 'media_links'

    def __str__(self):
        return f'{self.media_type} — {self.url}'
