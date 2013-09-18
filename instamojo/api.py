import json
import requests

class API:
    app_id = None
    token = None
    endpoint = None

    def __init__(self, app_id, token=None, endpoint=None):
        self.app_id = app_id
        self.token = token
        self.endpoint = endpoint

    def debug(self):
        return self._api_call('get', 'debug/')

    def auth(self, username, password):
        response = self._api_call(method='post', path='auth/', username=username, password=password)
        if response['success']:
            self.token = response['token']
            return self.token
        else:
            raise Exception(response['message']) # TODO: set custom exception?

    def offer_list(self):
        raise NotImplementedError('Dang!')

    def offer_detail(self, slug):
        raise NotImplementedError('Shite!')

    def offer_create(self, title, description=None, # Basic
                     base_price=None, currency=None, # Pricing
                     quantity=None, # Quantity
                     start_date=None, end_date=None, venue=None, timezone=None, # Event
                     redirect_url=None, # Redirect user to URL after successful payment
                     note=None, # Show note, embed in receipt after successful payment
                     upload_file=None, # File to upload
                     cover_image=None, # Cover image to associate with offer
                     ):
        raise NotImplementedError('Yikes!')

    def offer_edit(self, slug, # Need slug to identify offer
                     title=None, description=None, # Basic
                     base_price=None, currency=None, # Pricing
                     quantity=None, # Quantity
                     start_date=None, end_date=None, venue=None, timezone=None, # Event
                     redirect_url=None, # Redirect user to URL after successful payment
                     note=None, # Show note, embed in receipt after successful payment
                     upload_file=None, # File to upload
                     cover_image=None, # Cover image to associate with offer
                     ):
        raise NotImplementedError('Uh oh!')

    def offer_delete(self, slug):
        raise NotImplementedError('Shucks!')


    def _api_call(self, method, path, **kwargs):
        # Header: App-Id
        headers = {'X-App-Id': self.app_id}

        # If available, add the Auth-token to header
        if self.token:
            headers.update({'X-Auth-Token':self.token})

        # Build the URL for API call
        api_path = self.endpoint + path

        if method.upper() == 'GET':
            req = requests.get(api_path, data=kwargs, headers=headers)
        elif method.upper() == 'POST':
            req = requests.post(api_path, data=kwargs, headers=headers)
        elif method.upper() == 'DELETE':
            req = requests.delete(api_path, data=kwargs, headers=headers)
        elif method.upper() == 'PUT':
            req = requests.put(api_path, data=kwargs, headers=headers)
        elif method.upper() == 'PATCH':
            req = requests.patch(api_path, data=kwargs, headers=headers)
        else:
            raise Exception('Unable to make a API call for "%s" method.' % method)

        try:
            return json.loads(req.text)
        except:
            raise Exception('Unable to decode response. Expected JSON, got this: \n\n\n %s' % req.text)
