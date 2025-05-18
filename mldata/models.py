from django.db import models
from games.models import Game, Genre, Platform


class Mood(models.Model):
    """Модель для хранения настроений, связанных с играми."""
    name = models.CharField(max_length=50, unique=True, verbose_name='Название настроения')

    class Meta:
        db_table = 'moods'

    def __str__(self):
        return self.name


class GameGenreMLData(models.Model):
    """Модель для хранения данных по жанрам игр для машинного обучения."""
    game = models.ForeignKey(Game, related_name='genre_ml_data', on_delete=models.CASCADE, verbose_name='Игра')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    weight = models.FloatField(verbose_name='Вес')
    rating = models.FloatField(verbose_name='Рейтинг')
    rating_year = models.FloatField(verbose_name='Рейтинг за год')

    class Meta:
        db_table = 'game_genre_ml_data'
        unique_together = ('game', 'genre')


class GameMood(models.Model):
    """Модель для хранения отношений между играми и их настроениями."""
    game = models.ForeignKey(Game, related_name='moods', on_delete=models.CASCADE, verbose_name='Игра')
    mood = models.ForeignKey(Mood, on_delete=models.CASCADE, verbose_name='Настроение')

    class Meta:
        db_table = 'game_moods'
        unique_together = ('game', 'mood')


class GameSubgenreMLData(models.Model):
    """Модель для хранения данных по поджанрам игр для машинного обучения."""
    game = models.ForeignKey(Game, related_name='subgenre_ml_data', on_delete=models.CASCADE, verbose_name='Игра')
    subgenre = models.CharField(max_length=100, verbose_name='Поджанр')  # Или можно вынести в модель Subgenre
    weight = models.FloatField(verbose_name='Вес')
    rating = models.FloatField(verbose_name='Рейтинг')
    rating_year = models.FloatField(verbose_name='Рейтинг за год')

    class Meta:
        db_table = 'game_subgenre_ml_data'
        unique_together = ('game', 'subgenre')


class GamePlatformMLData(models.Model):
    """Модель для хранения данных по платформам игр для машинного обучения."""
    game = models.ForeignKey(Game, related_name='platform_ml_data', on_delete=models.CASCADE, verbose_name='Игра')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name='Платформа')
    rating = models.FloatField(verbose_name='Рейтинг')

    class Meta:
        db_table = 'game_platform_ml_data'
        unique_together = ('game', 'platform')
