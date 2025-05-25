import json
from django.test import TestCase, Client
from unittest.mock import patch

class MailingsViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('mailings.views.add_email_to_common_mailchimp_list')
    def test_add_email_to_common_success(self, mock_add_email):
        payload = {'email': 'test@example.com'}
        response = self.client.post(
            '/mailings/api/add_to_common_list/',  # учли префикс /mailings/
            data=json.dumps(payload),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        mock_add_email.assert_called_once_with(email='test@example.com')

    def test_add_email_to_common_missing_email(self):
        response = self.client.post(
            '/mailings/api/add_to_common_list/',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'success': False, 'message': 'Передайте email'})

    def test_add_email_to_common_bad_json(self):
        response = self.client.post(
            '/mailings/api/add_to_common_list/',
            data='not valid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'success': False, 'message': 'Неверный формат данных'})


    @patch('mailings.views.add_email_to_case_mailchimp_list')
    def test_add_email_to_case_success(self, mock_add_email):
        case_id = 123
        payload = {'email': 'caseuser@example.com'}
        response = self.client.post(
            f'/mailings/api/add_to_case_list/{case_id}/',
            data=json.dumps(payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})
        mock_add_email.assert_called_once_with(email='caseuser@example.com', case_id=case_id)

    def test_add_email_to_case_missing_email(self):
        case_id = 5
        response = self.client.post(
            f'/mailings/api/add_to_case_list/{case_id}/',
            data=json.dumps({}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'success': False, 'message': 'Передайте email'})

    def test_add_email_to_case_bad_json(self):
        case_id = 7
        response = self.client.post(
            f'/mailings/api/add_to_case_list/{case_id}/',
            data='invalid json',
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'success': False, 'message': 'Неверный формат данных'})