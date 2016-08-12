from unittest import TestCase

import responses

from instamojo_wrapper import Instamojo
from tests.payloads.refunds import refunds_payload


class TestPaymentRequests(TestCase):
    def setUp(self):
        self.api_endpoint = 'https://www.instamojo.com/api/1.1/'
        self.api = Instamojo('API-KEY', 'AUTH-TOKEN', self.api_endpoint)

    @responses.activate
    def test_refund_create(self):
        data = refunds_payload['refund_create']
        endpoint = self.api_endpoint + 'refunds/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.refund_create(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_refund_detail(self):
        data = refunds_payload['refund_detail']
        endpoint = self.api_endpoint + 'refunds/{id}/'.format(**data['request'])
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.refund_detail(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_refunds_list(self):
        data = refunds_payload['refunds_list']
        endpoint = self.api_endpoint + 'refunds/'
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.refunds_list(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)


