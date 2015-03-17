import os
import requests


class Instamojo(object):
    app_id = None
    auth_token = None
    endpoint = None

    def __init__(self, api_key, auth_token=None,
                 endpoint='https://www.instamojo.com/api/1.1/'):
        self.api_key = api_key
        self.auth_token = auth_token
        self.endpoint = endpoint

    def debug(self):
        return self._api_call(method='get', path='debug/')

    def auth(self, username, password):
        response = self._api_call(method='post', path='auth/',
                                  username=username, password=password)
        if response['success']:
            self.auth_token = response['auth_token']['auth_token']
            return self.auth_token
        else:
            raise Exception(response['message'])  # TODO: set custom exception?

    def links_list(self):
        response = self._api_call(method='get', path='links/')
        return response

    def link_detail(self, slug):
        response = self._api_call(method='get', path='links/%s/' % slug)
        return response

    def link_create(self, title=None,  # Title is not optional
                    description=None,  # Description is not optional
                    base_price=None,
                    currency=None,  # Pricing, is compulsory.
                    quantity=None,  # Quantity
                    start_date=None, end_date=None, venue=None,  # Event
                    timezone=None,
                    redirect_url=None,  # Redirect user to URL after successful payment
                    webhook_url=None,  # Ping your server with link data after successful payment
                    note=None,  # Show note, embed in receipt after successful payment
                    upload_file=None,  # File to upload
                    cover_image=None,  # Cover image to associate with link
                    enable_pwyw=None,  # Enable Pay What You Want
                    enable_sign=None,  # Enable Link Signing
                    socialpay_platforms=None,  # Choose platforms (twitter,facebook,linkedin)
                    ):

        file_upload_json = self._upload_if_needed(upload_file)
        cover_image_json = self._upload_if_needed(cover_image)

        link_data = dict(
            title=title,
            description=description,
            base_price=base_price,
            currency=currency,
            quantity=quantity,
            start_date=start_date,
            end_date=end_date,
            venue=venue,
            timezone=timezone,
            redirect_url=redirect_url,
            webhook_url=webhook_url,
            note=note,
            file_upload_json=file_upload_json,
            cover_image_json=cover_image_json,
            enable_pwyw=enable_pwyw,
            enable_sign=enable_sign,
            socialpay_platforms=socialpay_platforms,
        )
        response = self._api_call(method='post', path='links/', **link_data)
        return response

    def link_edit(self, slug,  # Need slug to identify link
                  title=None, description=None,  # Basic
                  base_price=None, currency=None,  # Pricing
                  quantity=None,  # Quantity
                  start_date=None, end_date=None, venue=None, timezone=None,  # Event
                  redirect_url=None,  # Redirect user to URL after successful payment
                  webhook_url=None,  # Ping your server with link data after successful payment
                  note=None,  # Show note, embed in receipt after successful payment
                  upload_file=None,  # File to upload
                  cover_image=None,  # Cover image to associate with link
                  enable_pwyw=None,  # Enable Pay What You Want
                  enable_sign=None,  # Enable Link Signing
                  socialpay_platforms=None,  # Choose platforms (twitter,facebook,linkedin)
                  ):
        """Only include the parameters that you wish to change."""
        file_upload_json = self._upload_if_needed(upload_file)
        cover_image_json = self._upload_if_needed(cover_image)

        link_data = dict(
            title=title,
            description=description,
            base_price=base_price,
            currency=currency,
            quantity=quantity,
            start_date=start_date,
            end_date=end_date,
            venue=venue,
            timezone=timezone,
            redirect_url=redirect_url,
            webhook_url=webhook_url,
            note=note,
            file_upload_json=file_upload_json,
            cover_image_json=cover_image_json,
            enable_pwyw=enable_pwyw,
            enable_sign=enable_sign,
            socialpay_platforms=socialpay_platforms,
        )
        response = self._api_call(method='patch', path='links/%s/' % slug, **link_data)
        return response

    def link_delete(self, slug):
        response = self._api_call(method='delete', path='links/%s/' % slug)
        return response

    def payments_list(self):
        response = self._api_call(method='get', path='payments/')
        return response

    def payment_detail(self, payment_id):
        response = self._api_call(method='get', path='payments/%s/' % payment_id)
        return response

    def _api_call(self, method, path, **kwargs):
        # Header: App-Id
        headers = {'X-Api-Key': self.api_key}

        # If available, add the Auth-token to header
        if self.auth_token:
            headers.update({'X-Auth-Token': self.auth_token})

        # Build the URL for API call
        api_path = self.endpoint + path

        # One last sanity check
        if not api_path.endswith('/'):
            api_path += '/'

        method = method.lower()
        if method not in ['get', 'post', 'delete', 'put', 'patch']:
            raise Exception('Unable to make a API call for %r method.' % method)

        # Picks up the right function to call (such as requests.get() for 'get')
        api_call = getattr(requests, method)
        req = api_call(api_path, data=kwargs, headers=headers)

        try:
            return req.json()
        except (TypeError, ValueError):
            raise Exception('Unable to decode response. Expected JSON, got this: \n\n\n %s' % req.text)

    def _get_file_upload_url(self):
        """Gets signed upload URL from server, use this to upload file."""
        response = self._api_call(method='GET', path='links/get_file_upload_url/')
        return response

    def _upload_file(self, filepath):
        """Helper function to upload file from local path."""
        file_upload_url = self._get_file_upload_url()['upload_url']

        filename = os.path.basename(filepath)
        files = {'fileUpload': (filename, open(filepath, 'rb'))}
        response = requests.post(file_upload_url, files=files)
        return response.text

    def _upload_if_needed(self, filepath):
        """If a file is found, uploads it and returns json, else returns None"""
        if filepath:
            return self._upload_file(filepath)
        return None  # Doesn't harm being explicit.
