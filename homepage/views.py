from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from games.models import Game, GameSimilarity  # Импортируем модели из приложения games


def home(request):
    # Получаем последние 5 игр по дате выпуска
    latest_games = Game.objects.order_by('-release_date')[:5]

    # Получаем избранные игры
    featured_games = Game.objects.filter(is_featured=True)

    # Подготовка данных для передачи в JSON-ответ
    def get_game_data(game):
        system_requirements = game.system_requirements
        similar_games = GameSimilarity.objects.filter(game=game).select_related('related_game')

        similar_game_data = [
            {
                'id': sim.related_game.id,
                'title': sim.related_game.title,
                'similarity_percent': sim.similarity_percent
            } for sim in similar_games
        ]

        return {
            'id': game.id,
            'title': game.title,
            'slug': game.slug,
            'slogan': game.slogan,
            'short_description': game.short_description,
            'release_date': game.release_date,
            'media_cover_image': game.media_cover_image,
            'metacritic_score': game.metacritic_score,
            'ign_score': game.ign_score,
            'system_requirements': {
                'cpu': system_requirements.cpu if system_requirements else None,
                'gpu': system_requirements.gpu if system_requirements else None,
                'ram': system_requirements.ram if system_requirements else None,
                'ssd': system_requirements.ssd if system_requirements else None,
                'os': system_requirements.os if system_requirements else None,
            },
            'similar_games': similar_game_data,
        }

    # Сбор данных для последних и избранных игр
    latest_games_data = [get_game_data(game) for game in latest_games]
    featured_games_data = [get_game_data(game) for game in featured_games]

    # Возвращаем JSON-ответ
    return JsonResponse({
        'latest_games': latest_games_data,
        'featured_games': featured_games_data,
    })
