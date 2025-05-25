from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from .services import add_email_to_common_mailchimp_list, \
    add_email_to_case_mailchimp_list


@csrf_exempt
@require_POST
def add_email_to_common_mailchimp_list_view(request):
    """Веб-сервис, добавляющий email в общий лист рассылки"""
    try:
        data = json.loads(request.body)
        email = data.get('email')
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Неверный формат данных'}, status=400)

    if not email:
        return JsonResponse({'success': False, 'message': 'Передайте email'}, status=400)

    add_email_to_common_mailchimp_list(email=email)
    return JsonResponse({'success': True})


@csrf_exempt
@require_POST
def add_email_to_case_mailchimp_list_view(request, pk):
    """Веб-сервис, добавляющий email в лист рассылок по конкретному делу"""
    try:
        data = json.loads(request.body)
        email = data.get('email')
        case_id = data.get('case_id')
    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'message': 'Неверный формат данных'}, status=400)

    if not email:
        return JsonResponse({'success': False, 'message': 'Передайте email'}, status=400)

    add_email_to_case_mailchimp_list(email=email, case_id=pk)

    return JsonResponse({'success': True})
