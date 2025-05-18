from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Game


def game_list_api(request):
    """API: Список всех игр"""
    games = Game.objects.prefetch_related('developers', 'publishers', 'genres', 'platforms').all()
    data = [
        {
            'id': game.id,
            'title': game.title,
            'slug': game.slug,
            'slogan': game.slogan,
            'short_description': game.short_description,
            'description': game.description,
            'release_date': game.release_date,
            'is_featured': game.is_featured,
            'favourite': game.favourite,
            'is_top_in_year': game.is_top_in_year,
            'is_top_in_genre': game.is_top_in_genre,
            'trending': game.trending,
            'metacritic_score': game.metacritic_score,
            'ign_score': game.ign_score,
            'score': game.score,
            'media_cover_image': game.media_cover_image,
            'media_background_video': game.media_background_video,
            'screenshots': game.screenshots.split(',') if game.screenshots else [],
            'trailers': game.trailers.split(',') if game.trailers else [],
            'alt_genres': game.alt_genres,
            'developers': [{'id': dev.id, 'name': dev.name} for dev in game.developers.all()],
            'publishers': [{'id': pub.id, 'name': pub.name} for pub in game.publishers.all()],
            'genres': [{'id': genre.id, 'name': genre.name} for genre in game.genres.all()],
            'platforms': [{'id': platform.id, 'name': platform.name} for platform in game.platforms.all()],
            'system_requirements': {
                'cpu': game.system_requirements.cpu if game.system_requirements else None,
                'gpu': game.system_requirements.gpu if game.system_requirements else None,
                'ram': game.system_requirements.ram if game.system_requirements else None,
                'ssd': game.system_requirements.ssd if game.system_requirements else None,
                'os': game.system_requirements.os if game.system_requirements else None,
            } if game.system_requirements else None,
        }
        for game in games
    ]
    return JsonResponse({'games': data})


def game_detail_api(request, pk):
    """API: Детали конкретной игры по ID"""
    game = get_object_or_404(Game, pk=pk)
    data = {
        'id': game.id,
        'title': game.title,
        'slug': game.slug,
        'slogan': game.slogan,
        'short_description': game.short_description,
        'description': game.description,
        'release_date': game.release_date,
        'is_featured': game.is_featured,
        'favourite': game.favourite,
        'is_top_in_year': game.is_top_in_year,
        'is_top_in_genre': game.is_top_in_genre,
        'trending': game.trending,
        'metacritic_score': game.metacritic_score,
        'ign_score': game.ign_score,
        'score': game.score,
        'media_cover_image': game.media_cover_image,
        'media_background_video': game.media_background_video,
        'screenshots': game.screenshots.split(',') if game.screenshots else [],
        'trailers': game.trailers.split(',') if game.trailers else [],
        'alt_genres': game.alt_genres,
        'developers': [{'id': dev.id, 'name': dev.name} for dev in game.developers.all()],
        'publishers': [{'id': pub.id, 'name': pub.name} for pub in game.publishers.all()],
        'genres': [{'id': genre.id, 'name': genre.name} for genre in game.genres.all()],
        'platforms': [{'id': platform.id, 'name': platform.name} for platform in game.platforms.all()],
        'system_requirements': {
            'cpu': game.system_requirements.cpu if game.system_requirements else None,
            'gpu': game.system_requirements.gpu if game.system_requirements else None,
            'ram': game.system_requirements.ram if game.system_requirements else None,
            'ssd': game.system_requirements.ssd if game.system_requirements else None,
            'os': game.system_requirements.os if game.system_requirements else None,
        } if game.system_requirements else None,
    }
    return JsonResponse({'game': data})
