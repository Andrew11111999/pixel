from django.db import models


class Developer(models.Model):
    """Модель, представляющая разработчика игры."""
    name = models.CharField(max_length=255, unique=True, verbose_name='Название разработчика')

    class Meta:
        db_table = 'developers'

    def __str__(self):
        return self.name


class Publisher(models.Model):
    """Модель, представляющая издателя игры."""
    name = models.CharField(max_length=255, unique=True, verbose_name='Название издателя')

    class Meta:
        db_table = 'publishers'

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Модель, представляющая жанр игры."""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название жанра')

    class Meta:
        db_table = 'genres'

    def __str__(self):
        return self.name


class Platform(models.Model):
    """Модель, представляющая платформу, на которой доступна игра."""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название платформы')

    class Meta:
        db_table = 'platforms'

    def __str__(self):
        return self.name


class SystemRequirement(models.Model):
    """Модель, представляющая системные требования для игры."""
    cpu = models.CharField(max_length=255, blank=True, verbose_name='Процессор')
    gpu = models.CharField(max_length=255, blank=True, verbose_name='Видеокарта')
    ram = models.CharField(max_length=255, blank=True, verbose_name='Оперативная память')
    ssd = models.CharField(max_length=255, blank=True, verbose_name='Необходимый диск (SSD)')
    os = models.CharField(max_length=255, blank=True, verbose_name='Операционная система')

    class Meta:
        db_table = 'system_requirements'

    def __str__(self):
        return f'CPU: {self.cpu}, GPU: {self.gpu}'


class Game(models.Model):
    """Модель, представляющая игру."""
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=255, verbose_name='Название игры')
    slug = models.SlugField(unique=True, verbose_name='Слаг игры')
    slogan = models.CharField(max_length=255, blank=True, verbose_name='Слоган')
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    description = models.TextField(blank=True, verbose_name='Описание')
    release_date = models.DateField(verbose_name='Дата выхода')
    is_featured = models.BooleanField(default=False, verbose_name='Избранная игра')
    favourite = models.BooleanField(default=False, verbose_name='Избранное')
    is_top_in_year = models.BooleanField(default=False, verbose_name='Топ в этом году')
    is_top_in_genre = models.BooleanField(default=False, verbose_name='Топ в жанре')
    trending = models.BooleanField(default=False, verbose_name='Трендовая игра')
    metacritic_score = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Рейтинг Metacritic')
    ign_score = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name='Рейтинг IGN')
    score = models.FloatField(null=True, blank=True, verbose_name='Общий рейтинг')
    media_cover_image = models.URLField(blank=True, verbose_name='Ссылка на обложку')
    media_background_video = models.URLField(blank=True, verbose_name='Ссылка на фоновое видео')
    screenshots = models.TextField(blank=True, help_text='Ссылки на скриншоты через запятую', verbose_name='Скриншоты')
    trailers = models.TextField(blank=True, help_text='Ссылки на трейлеры через запятую', verbose_name='Трейлеры')
    alt_genres = models.CharField(max_length=255, blank=True, verbose_name='Альтернативные жанры')
    developers = models.ManyToManyField(Developer, related_name='games', verbose_name='Разработчики')
    publishers = models.ManyToManyField(Publisher, related_name='games', verbose_name='Издатели')
    genres = models.ManyToManyField(Genre, related_name='games', verbose_name='Жанры')
    platforms = models.ManyToManyField(Platform, related_name='games', verbose_name='Платформы')
    system_requirements = models.OneToOneField(SystemRequirement, null=True, blank=True, on_delete=models.SET_NULL,
                                               verbose_name='Системные требования')

    class Meta:
        db_table = 'games'

    def __str__(self):
        return self.title


class GameSimilarity(models.Model):
    """Модель для хранения информации о похожих играх."""
    game = models.ForeignKey(Game, related_name='similar_games_from', on_delete=models.CASCADE, verbose_name='Игра')
    related_game = models.ForeignKey(Game, related_name='similar_games_to', on_delete=models.CASCADE,
                                     verbose_name='Похожая игра')
    similarity_percent = models.PositiveSmallIntegerField(verbose_name='Процент схожести')

    class Meta:
        db_table = 'game_similarities'
        unique_together = ('game', 'related_game')

    def __str__(self):
        return f'{self.game.slug} ~ {self.related_game.slug}: {self.similarity_percent}%'


