from dataclasses import fields
from typing import Optional

from mailchimp3 import MailChimp

from django.conf import settings


def add_mailchimp_email_with_tag(audience_name: str, email: str, tag: str) -> None:
    """Добавляет в Mailchimp email в аудиторию с названием audience_name"""
    _add_email_to_mailchimp_audience(audience_id=settings.MAILCHIMP_AUDIENCES.get(audience_name),
                                     email=email)
    _add_mailchimp_tag(audience_id=settings.MAILCHIMP_COMMON_LIST_ID,
                       subscriber_hash=_get_mailchimp_subscriber_hash(email),
                       tag=tag)


def _get_mailchimp_client() -> MailChimp:
    """Возвращает клиент API для работы с Mailchimp"""
    return MailChimp(
        mc_api=settings.MAILCHIMP_API_KEY,
        mc_user=settings.MAILCHIMP_USERNAME)


def _add_email_to_mailchimp_audience(audience_id: str, email: str) -> None:
    """Добавляет email в Mailchimp аудиторию с идентификатором audience_id"""
    _get_mailchimp_client().lists.members.create(audience_id, {
        'email_address': email,
        'status': 'subscribed'
    })


def _get_mailchimp_subscriber_hash(email: str) -> Optional[str]:
    """Возвращает идентификатор email'a в Mailchimp или None,
     если email там не найден"""
    members = _get_mailchimp_client() \
        .search_members \
        .get(query=email,
             fields='exact_matches.members.id') \
        .get('exact_matches').get('members')
    if not members:
        return None
    return members[0].get('id')


def _add_mailchimp_tag(audience_id: str, subscriber_hash: str, tag: str) -> None:
    """Добавляет тег tag для email'a с идентификатором subscriber_hash в аудитории audience_id"""
    _get_mailchimp_client().lists.members.tags.update(
        list_id=audience_id,
        subscriber_hash=subscriber_hash,
        data={'tags': [{'name': tag, 'status': 'active'}]})
