from . import BaseTestClass
try:
    from urllib import urlencode
    from urlparse import parse_qsl, urlparse
except ImportError:
    from urllib.parse import parse_qsl, urlencode, urlparse

import responses

from instamojo_wrapper import Instamojo
from tests.payloads import payment_requests_payload


class TestPaymentRequests(BaseTestClass):
    def setUp(self):
        self.api_endpoint = 'https://www.instamojo.com/api/1.1/'
        self.api = Instamojo('API-KEY', 'AUTH-TOKEN', self.api_endpoint)

    @responses.activate
    def test_payment_request_create(self):
        data = payment_requests_payload['payment_request_create']
        endpoint = self.api_endpoint + 'payment-requests/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.payment_request_create(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_payment_request_status(self):
        data = payment_requests_payload['payment_request_status']
        endpoint = self.api_endpoint + 'payment-requests/{id}/'.format(**data['request'])
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.payment_request_status(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_payment_requests_list(self):
        data = payment_requests_payload['payment_requests_list']
        endpoint = self.api_endpoint + 'payment-requests/'
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.payment_requests_list(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_payment_requests_list_optional_params(self):
        data = payment_requests_payload['payment_requests_list_optional_params']
        endpoint = self.api_endpoint + 'payment-requests/'
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.payment_requests_list(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        parsed_url = urlparse(responses.calls[0].request.url)
        self.assertTrue(endpoint.endswith(parsed_url.path))
        self.assertDictEqual(dict(parse_qsl(parsed_url.query.strip('/'))), data['request'])

    @responses.activate
    def test_payment_request_payment_status(self):
        data = payment_requests_payload['payment_request_payment_status']
        endpoint = self.api_endpoint + 'payment-requests/{id}/{payment_id}/'.format(**data['request'])
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.payment_request_payment_status(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)
