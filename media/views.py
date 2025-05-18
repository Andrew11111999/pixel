from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import MediaLink

def media_list_api(request):
    """API: Список всех медиа ссылок"""
    medias = Media.objects.select_related('game').all()
    data = [
        {
            'id': media.id,
            'game': {
                'id': media.game.id,
                'title': media.game.title,
                'slug': media.game.slug,
            } if media.game else None,
            'media_type': media.media_type,
            'url': media.url,
        }
        for media in medias
    ]
    return JsonResponse({'media_links': data})

def media_detail_api(request, pk):
    """API: Детали конкретного медиа по ID"""
    media = get_object_or_404(Media, pk=pk)
    data = {
        'id': media.id,
        'game': {
            'id': media.game.id,
            'title': media.game.title,
            'slug': media.game.slug,
        } if media.game else None,
        'media_type': media.media_type,
        'url': media.url,
    }
    return JsonResponse({'media_link': data})
