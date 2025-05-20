from django.http import JsonResponse
from .models import StaticContent
from games.models import Game


def home(request):
    # Получаем статический контент
    static_content = StaticContent.objects.all()
    static_data = [
        {'title': content.title, 'content': content.content, 'image': content.image.url if content.image else None} for
        content in static_content]

    # Получаем динамический контент (например, последние игры)
    latest_games = Game.objects.order_by('-created_at')[:5]
    games_data = list(latest_games.values('id', 'title', 'description'))

    return JsonResponse({
        'static_content': static_data,
        'latest_games': games_data
    })
