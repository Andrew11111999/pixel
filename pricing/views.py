from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import OriginPrice, Pricing


def pricing_list_api(request):
    """API: список всех цен"""
    prices_qs = OriginPrice.objects.select_related('game').all()
    data = [
        {
            'id': price.id,
            'origin_name': price.origin_name,
            'buy_link': price.buy_link,
            'price': str(price.price),  # Decimal -> str для JSON
            'game': {
                'id': price.game.id,
                'title': price.game.title,
                'slug': price.game.slug,
            } if price.game else None,
        }
        for price in prices_qs
    ]
    return JsonResponse({'pricing': data})


def pricing_detail_api(request, pk):
    """API: получить детали конкретной цены по ID"""
    price = get_object_or_404(OriginPrice, pk=pk)
    data = {
        'id': price.id,
        'origin_name': price.origin_name,
        'buy_link': price.buy_link,
        'price': str(price.price),
        'game': {
            'id': price.game.id,
            'title': price.game.title,
            'slug': price.game.slug,
        } if price.game else None,
    }
    return JsonResponse({'pricing': data})
