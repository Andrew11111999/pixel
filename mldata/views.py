from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import (
    GameGenreMLData,
    GameMood,
    GameSubgenreMLData,
    GamePlatformMLData,
)
# Импорт модели Game для связных данных
from games.models import Game, Genre, Platform


# --- MLData по жанрам ---
def ml_genre_list_api(request):
    qs = GameGenreMLData.objects.select_related('game', 'genre')
    data = [
        {
            'id': item.id,
            'game': {
                'id': item.game.id,
                'title': item.game.title,
                'slug': item.game.slug,
            } if item.game else None,
            'genre': {
                'id': item.genre.id,
                'name': item.genre.name,
            } if item.genre else None,
            'weight': item.weight,
            'rating': item.rating,
            'rating_year': item.rating_year,
        }
        for item in qs
    ]
    return JsonResponse({'data': data})


def ml_genre_detail_api(request, pk):
    item = get_object_or_404(GameGenreMLData, pk=pk)
    data = {
        'id': item.id,
        'game': {
            'id': item.game.id,
            'title': item.game.title,
            'slug': item.game.slug,
        } if item.game else None,
        'genre': {
            'id': item.genre.id,
            'name': item.genre.name,
        } if item.genre else None,
        'weight': item.weight,
        'rating': item.rating,
        'rating_year': item.rating_year,
    }
    return JsonResponse({'data': data})


# --- MLData по настройкам (мудсам) ---
def ml_moods_list_api(request):
    qs = GameMood.objects.select_related('game', 'mood')
    data = [
        {
            'id': item.id,
            'game': {
                'id': item.game.id,
                'title': item.game.title,
                'slug': item.game.slug,
            } if item.game else None,
            'mood': {
                'id': item.mood.id,
                'name': item.mood.name,
            } if item.mood else None,
        }
        for item in qs
    ]
    return JsonResponse({'data': data})


def ml_mood_detail_api(request, pk):
    item = get_object_or_404(GameMood, pk=pk)
    data = {
        'id': item.id,
        'game': {
            'id': item.game.id,
            'title': item.game.title,
            'slug': item.game.slug,
        } if item.game else None,
        'mood': {
            'id': item.mood.id,
            'name': item.mood.name,
        } if item.mood else None,
    }
    return JsonResponse({'data': data})


# --- MLData по поджанрам ---
def ml_subgenre_list_api(request):
    qs = GameSubgenreMLData.objects.select_related('game')
    data = [
        {
            'id': item.id,
            'game': {
                'id': item.game.id,
                'title': item.game.title,
                'slug': item.game.slug,
            } if item.game else None,
            'subgenre': item.subgenre,
            'weight': item.weight,
            'rating': item.rating,
            'rating_year': item.rating_year,
        }
        for item in qs
    ]
    return JsonResponse({'data': data})


def ml_subgenre_detail_api(request, pk):
    item = get_object_or_404(GameSubgenreMLData, pk=pk)
    data = {
        'id': item.id,
        'game': {
            'id': item.game.id,
            'title': item.game.title,
            'slug': item.game.slug,
        } if item.game else None,
        'subgenre': item.subgenre,
        'weight': item.weight,

        'rating': item.rating,
        'rating_year': item.rating_year,
    }
    return JsonResponse({'data': data})


# --- MLData по платформам ---
def ml_platform_list_api(request):
    qs = GamePlatformMLData.objects.select_related('game', 'platform')
    data = [
        {
            'id': item.id,
            'game': {
                'id': item.game.id,
                'title': item.game.title,
                'slug': item.game.slug,
            } if item.game else None,
            'platform': {
                'id': item.platform.id,
                'name': item.platform.name,
            } if item.platform else None,
            'rating': item.rating,
        }
        for item in qs
    ]
    return JsonResponse({'data': data})


def ml_platform_detail_api(request, pk):
    item = get_object_or_404(GamePlatformMLData, pk=pk)
    data = {
        'id': item.id,
        'game': {
            'id': item.game.id,
            'title': item.game.title,
            'slug': item.game.slug,
        } if item.game else None,
        'platform': {
            'id': item.platform.id,
            'name': item.platform.name,
        } if item.platform else None,
        'rating': item.rating,
    }
    return JsonResponse({'data': data})
