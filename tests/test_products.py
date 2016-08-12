from unittest import TestCase

import responses
from mock import mock_open, patch

from instamojo_wrapper import Instamojo
from tests.payloads.products import products_payload


class Testproducts_payload(TestCase):
    def setUp(self):
        self.api_endpoint = 'https://www.instamojo.com/api/1.1/'
        self.api = Instamojo('API-KEY', 'AUTH-TOKEN', self.api_endpoint)

    @responses.activate
    def test_basic_product_creation(self):
        data = products_payload['basic_product_creation']
        endpoint = self.api_endpoint + 'links/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.link_create(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_event_product_creation(self):
        data = products_payload['event_product_creation']
        endpoint = self.api_endpoint + 'links/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.link_create(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(
            responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_digital_product_creation(self):
        data = products_payload['digital_product_creation']
        endpoint = self.api_endpoint + 'links/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        get_file_upload_url_endpoint = self.api_endpoint + 'links/get_file_upload_url/'
        file_upload_endpoint = self.api_endpoint + 'links/upload/'
        responses.add(
            responses.GET,
            get_file_upload_url_endpoint,
            json={'upload_url': file_upload_endpoint}
        )
        responses.add(
            responses.POST,
            self.api_endpoint + 'links/upload/',
            body='{"spam": "eggs"}'
        )
        with patch('instamojo_wrapper.api.open', mock_open(), create=True) as m:
            resp = self.api.link_create(**data['request'])
            self.assertEqual(resp, {})
            self.assertEqual(len(responses.calls), 3)
            self.assertEqual(
                responses.calls[0].request.url, get_file_upload_url_endpoint)
            self.assertEqual(
                responses.calls[1].request.url, file_upload_endpoint)
            self.assertEqual(
                responses.calls[2].request.url, endpoint)
            m.assert_called_once_with(data['request']['file_upload'], 'rb')

    @responses.activate
    def test_product_creation_with_cover_image(self):
        data = products_payload['product_creation_with_cover_image']
        endpoint = self.api_endpoint + 'links/'
        get_file_upload_url_endpoint = self.api_endpoint + 'links/get_file_upload_url/'
        file_upload_endpoint = self.api_endpoint + 'links/upload/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        responses.add(
            responses.GET,
            get_file_upload_url_endpoint,
            json={'upload_url': file_upload_endpoint}
        )
        responses.add(
            responses.POST,
            self.api_endpoint + 'links/upload/',
            body='{"spam": "eggs"}'
        )
        with patch('instamojo_wrapper.api.open', mock_open(), create=True) as m:
            resp = self.api.link_create(**data['request'])
            self.assertEqual(resp, {})
            self.assertEqual(len(responses.calls), 3)
            self.assertEqual(
                responses.calls[0].request.url, get_file_upload_url_endpoint)
            self.assertEqual(
                responses.calls[1].request.url, file_upload_endpoint)
            self.assertEqual(
                responses.calls[2].request.url, endpoint)
            m.assert_called_once_with(data['request']['cover_image'], 'rb')

    @responses.activate
    def test_product_creation_with_all_params(self):
        data = products_payload['product_creation_with_all_params']
        endpoint = self.api_endpoint + 'links/'
        get_file_upload_url_endpoint = self.api_endpoint + 'links/get_file_upload_url/'
        file_upload_endpoint = self.api_endpoint + 'links/upload/'
        responses.add(
            responses.POST,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        responses.add(
            responses.GET,
            get_file_upload_url_endpoint,
            json={'upload_url': file_upload_endpoint}
        )
        responses.add(
            responses.POST,
            file_upload_endpoint,
            body='{"spam": "eggs"}'
        )
        with patch('instamojo_wrapper.api.open', mock_open(), create=True) as m:
            resp = self.api.link_create(**data['request'])
            self.assertEqual(resp, {})
            self.assertEqual(len(responses.calls), 5)
            self.assertEqual(
                responses.calls[0].request.url, get_file_upload_url_endpoint)
            self.assertEqual(
                responses.calls[1].request.url, file_upload_endpoint)
            self.assertEqual(
                responses.calls[2].request.url, get_file_upload_url_endpoint)
            self.assertEqual(
                responses.calls[3].request.url, file_upload_endpoint)
            self.assertEqual(
                responses.calls[4].request.url, endpoint)
            m.assert_any_call(data['request']['cover_image'], 'rb')
            m.assert_any_call(data['request']['file_upload'], 'rb')

    @responses.activate
    def test_product_edit_with_all_params(self):
        data = products_payload['product_edit_with_all_params']
        endpoint = self.api_endpoint + 'links/{slug}/'.format(slug=data['request']['slug'])
        get_file_upload_url_endpoint = self.api_endpoint + 'links/get_file_upload_url/'
        file_upload_endpoint = self.api_endpoint + 'links/upload/'
        responses.add(
            responses.PATCH,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        responses.add(
            responses.GET,
            get_file_upload_url_endpoint,
            json={'upload_url': file_upload_endpoint}
        )

        responses.add(
            responses.POST,
            file_upload_endpoint,
            body='{"spam": "eggs"}'
        )
        with patch('instamojo_wrapper.api.open', mock_open(), create=True) as m:
            resp = self.api.link_edit(**data['request'])
            self.assertEqual(resp, {})
            self.assertEqual(len(responses.calls), 5)
            self.assertEqual(
                responses.calls[0].request.url, get_file_upload_url_endpoint)
            self.assertEqual(
                responses.calls[1].request.url, file_upload_endpoint)
            self.assertEqual(
                responses.calls[2].request.url, get_file_upload_url_endpoint)
            self.assertEqual(
                responses.calls[3].request.url, file_upload_endpoint)
            self.assertEqual(responses.calls[4].request.url, endpoint)
            m.assert_any_call(data['request']['cover_image'], 'rb')
            m.assert_any_call(data['request']['file_upload'], 'rb')

    @responses.activate
    def test_product_delete(self):
        data = products_payload['product_delete']
        endpoint = self.api_endpoint + 'links/{slug}/'.format(slug=data['request']['slug'])
        exception = Exception('Unable to decode response. Expected JSON, got this: \n\n\n ')
        responses.add(
            responses.DELETE,
            endpoint,
            body=exception
        )
        self.assertRaises(type(exception), self.api.link_delete, **data['request'])
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_product_details(self):
        data = products_payload['product_details']
        endpoint = self.api_endpoint + 'links/{slug}/'.format(slug=data['request']['slug'])
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.link_detail(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_product_details(self):
        data = products_payload['product_details']
        endpoint = self.api_endpoint + 'links/{slug}/'.format(slug=data['request']['slug'])
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.link_detail(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, endpoint)

    @responses.activate
    def test_products_payload_list(self):
        data = products_payload['products_list']
        endpoint = self.api_endpoint + 'links/'
        responses.add(
            responses.GET,
            endpoint,
            body='{}',
            content_type='application/json'
        )
        resp = self.api.links_list(**data['request'])
        self.assertEqual(resp, {})
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url, endpoint)
