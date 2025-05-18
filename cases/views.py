from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Case


def case_list_api(request):
    """API: Список всех дел"""
    cases = Case.objects.all()
    data = [
        {
            'id': case.id,
            'name': case.name,
        }
        for case in cases
    ]
    return JsonResponse({'cases': data})


def case_detail_api(request, pk):
    """API: Детали конкретного дела по ID"""
    case = get_object_or_404(Case, pk=pk)
    data = {
        'id': case.id,
        'name': case.name,
    }
    return JsonResponse({'case': data})
