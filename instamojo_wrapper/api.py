import os
import requests
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


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
                    currency='INR',
                    quantity=None,  # Quantity
                    start_date=None, end_date=None, venue=None,  # Event
                    timezone=None,
                    redirect_url=None,  # Redirect user to URL after successful payment
                    webhook_url=None,  # Ping your server with link data after successful payment
                    note=None,  # Show note, embed in receipt after successful payment
                    upload_file=None,  # File to upload
                    file_upload=None,  # File to upload (correct param as per documentation)
                    cover_image=None,  # Cover image to associate with link
                    enable_pwyw=None,  # Enable Pay What You Want
                    enable_sign=None,  # Enable Link Signing
                    socialpay_platforms=None,  # Choose platforms (twitter,facebook,linkedin)
                    ):

        if file_upload:
            upload_file = file_upload
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
                  file_upload=None,  # File to upload (correct param as per documentation)
                  cover_image=None,  # Cover image to associate with link
                  enable_pwyw=None,  # Enable Pay What You Want
                  enable_sign=None,  # Enable Link Signing
                  socialpay_platforms=None,  # Choose platforms (twitter,facebook,linkedin)
                  ):
        """Only include the parameters that you wish to change."""
        if file_upload:
            upload_file = file_upload
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

    # ##### Request a Payment ######

    def payment_request_create(
        self,
        purpose,
        amount,
        buyer_name=None,
        email=None,
        phone=None,
        send_email=False,
        send_sms=False,
        redirect_url=None,
        webhook=None,
        allow_repeated_payments=True
    ):
        """
        Create a Payment Request

        Parameters
        __________
        purpose : str
            Purpose of the payment.
        amount : str
            Amount to be paid.
        buyer_name : str, optional
            Name of the buyer, can be used for prefilling the form.
        email : str, optional
            Email of the payer.
        phone : str, optional
            Phone number of payer.
        send_email : bool, optional
            Set this to True if you want to send email to the payer if email is specified.
            If email is not specified then an error is raised(default value: False)
        send_sms : bool, optional
            Set this to True if you want to send SMS to the payer if phone is specified.
            If phone is not specified then an error is raised. (default value: False)
        redirect_url : str, optional
            Set this to a thank-you or sorry page on your site.
            Buyers will be redirected here after successfulor failed payment.
        webhook : str, optional
            Set this to a URL that can accept POST requests made by Instamojo server
            after successful or failed payment.
        allow_repeated_payments : bool, optional
            To disallow multiple successful payments on a Payment Request pass false for this field.
            If this is set to false then the link is not accessible publicly after first successful
            payment, though you can still access it using API(default value: True).

        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'payment_request': {'id': '...', ...}
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """
        payment_request_data = dict(
            purpose=purpose,
            amount=amount,
            buyer_name=buyer_name,
            email=email,
            phone=phone,
            send_email=send_email,
            send_sms=send_sms,
            redirect_url=redirect_url,
            webhook=webhook,
            allow_repeated_payments=allow_repeated_payments
        )
        response = self._api_call(method='post', path='payment-requests/', **payment_request_data)
        return response

    def payment_request_status(self, id):
        """
        Get the status or details of a payment request.

        Parameters
        __________
        id : str
            The unique ID of a payment request, this is the 'id' key returned by
            `payment_request_create()` request. The 'id' key is inside the
            'refund_create' dict.

        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'payment_request': {'id': '...',
                                                                    'payments': [...],
                                                                    ...
                                                                   }
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

            If the request is successful then the 'payment_request' dict will now also
            contain an additional key named 'payments'. That's a list contain payments related
            to this payment request.

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """
        path = 'payment-requests/{id}/'.format(id=id)
        response = self._api_call(method='get', path=path)
        return response

    def payment_request_payment_status(self, id, payment_id):
        """
        Get the details of a payment related to payment request.

        Parameters
        __________
        id : str
            The unique ID of a payment request, this is the 'id' key returned by
            `payment_request_create()` request. The 'id' key is inside the
            'refund_create' dict.

        payment_id : str
            ID of a payment, this is the 'payment_id' key returned with the
            redirection URL and/or webhook.

        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'payment_request': {'id': '...',
                                                                    'payment': {},
                                                                    ...
                                                                   }
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

            If the request is successful then the 'payment_request' dict will now also
            contain an additional key named 'payment'. This dict contains the details
            of the payment.

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """
        path = 'payment-requests/{id}/{payment_id}/'.format(id=id, payment_id=payment_id)
        response = self._api_call(method='get', path=path)
        return response

    def payment_requests_list(
        self,
        min_created_at=None,
        max_created_at=None,
        min_modified_at=None,
        max_modified_at=None,
    ):
        """
        Get a list of all Payment requests.

        Parameters
        __________
        min_created_at, max_created_at, min_modified_at, max_modified_at: str, optional
            These optional arguments can be used to filter the list of payments by their
            'created_at' and 'modified_at' keys.

            For example if you pass min_created_at = '2015-07-02' and max_created_at = '2015-07-10'
            then this request will return all the payment requests made on and after 2015-07-02 and
            before and on 2015-07-10.

            Details related to support datetime formats can be found in the documentation:
            https://www.instamojo.com/developers/request-a-payment-api/#toc-filtering-payment-requests

        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'payment_requests': [{'id': '...', ...},
                                                                     {'id': '...', ...}]
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

            Note that the 'payments' related to individual Payment Request is not
            returned by this request.

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """
        path = 'payment-requests/'
        query_dict = dict(
            min_created_at=min_created_at,
            max_created_at=max_created_at,
            min_modified_at=min_modified_at,
            max_modified_at=max_modified_at,
        )
        query_string = urlencode(dict((k, v) for k, v in query_dict.items() if v is not None))
        if query_string:
            path += '?' + query_string
        response = self._api_call(method='get', path=path)
        return response

    # ##### Refunds ######

    def refund_create(
        self,
        payment_id,
        type,
        body,
        refund_amount=None
    ):
        """
        Create a new Refund

        Parameters
        __________
        payment_id : str
            Payment ID for which Refund is being requested.
        type : str
            A three letter short-code to identify the type of the refund. Check the
            REST docs for more info on the allowed values.
        body : str
            Additional explanation related to why this refund is being requested.
        refund_amount : str, optional
            This field can be used to specify the refund amount. For instance, you
            may want to issue a refund for an amount lesser than what was paid. If
            this field is not provided then the total transaction amount is going to
            be used.


        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'refund': {'id': '...', ...}
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """
        refund_request_data = dict(
            payment_id=payment_id,
            type=type,
            body=body
        )
        if refund_amount is not None:
            refund_request_data['refund_amount'] = refund_amount

        response = self._api_call(method='post', path='refunds/', **refund_request_data)
        return response

    def refund_detail(self, id):
        """
        Get details of a Refund.

        Parameters
        __________
        id : str
            The unique ID of a refund, this is the 'id' key returned by
            `refund_create()` request. The 'id' key is inside the 'refund' dict.

        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'refund': {'id': '...', ...}
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """
        response = self._api_call(method='get', path='refunds/{id}/'.format(id=id))
        return response

    def refunds_list(self):
        """
        Get list of all Refunds.

        Returns
        _______
        dict
            This will contain the response from Instamojo.
            The two possible outputs are:
                1. When request is successful: {'success': True,
                                                'refunds': [{'id': '...', ...},
                                                           {'id': '...', ...}]
                                               }
                2. When Request failed: {'success': False, 'message': '...'}

        Raises
        ______
        Exception
            If the request failed due to some reason, network error etc.
        """

        response = self._api_call(method='get', path='refunds/')
        return response
