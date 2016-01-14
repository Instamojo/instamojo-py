## Request a Payment

### Create a new Payment Request

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Payment Request
    response = api.payment_request_create(
        amount='3499',
        purpose='FIFA 16',
        send_email=True,
        email="foo@example.com",
        redirect_url="http://www.example.com/handle_redirect.py"
        )
    # print the long URL of the payment request.
    print response['payment_request']['longurl']
    # print the unique ID(or payment request ID)
    print response['payment_request']['id']

### Get the status or details of a Payment Request

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Payment Request
    response = api.payment_request_status('[PAYMENT REQUEST ID]')

    print response['payment_request']['shorturl']  # Get the short URL
    print response['payment_request']['status']    # Get the current status
    print response['payment_request']['payments']  # List of payments


### Get the status of a Payment related to a Payment Request

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Payment Request
    response = api.payment_request_payment_status('[PAYMENT REQUEST ID]', '[PAYMENT ID]')

    print response['payment_request']['purpose']             # Purpose of Payment Request
    print response['payment_request']['payment']['status']   # Payment status


### Get a list of all Payment Requests

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Payment Request
    response = api.payment_request_list()

    # Loop over all of the payment requests
    for payment_request in response['payment_requests']:
        print payment_request['status']

`payment_request_list()` also accepts optional arguments like `max_created_at`, `min_created_at`, `min_modified_at` and `max_modified_at` for filtering the list of Payment Requests. Note that it is not required to pass all of them.

    response = api.payment_request_list(max_created_at="2015-11-19T10:12:19Z",
                                        min_created_at="2015-10-29T12:51:36Z")

For details related to supported datetime format supported by these arguments check the documentation: https://www.instamojo.com/developers/request-a-payment-api/#toc-filtering-payment-requests

## Available Request a Payment Functions

 * `payment_request_create(purpose, amount)` => Payment Request
 * `payment_request_status(id)` => Payment Request
 * `payment_request_list()` => List of Payment Requests
 * `payment_request_payment_status(id, payment_id)` => Payment Request with Payment details

## Payment Request Creation Parameters

### Required
  * `purpose`: Purpose of the payment request. (max-characters: 30)
  * `amount`: Amount requested (min-value: 9 ; max-value: 200000)

### Optional
  * `buyer_name`: Name of the payer. (max-characters: 100)
  * `email`: Email of the payer. (max-characters: 75)
  * `phone`: Phone number of the payer.
  * `send_email`: Set this to True if you want to send email to the payer if email is specified. If email is not specified then an error is raised. (default value: `False`)
  * `send_sms`: Set this to True if you want to send SMS to the payer if phone is specified. If phone is not specified then an error is raised. (default value: `False`)
  * `redirect_url`: set this to a thank-you page on your site. Buyers will be redirected here after successful payment.
  * `webhook`: set this to a URL that can accept POST requests made by Instamojo server after successful payment.
  * `allow_repeated_payments`: To disallow multiple successful payments on a Payment Request pass `false` for this field. If this is set to `false` then the link is not accessible publicly after first successful payment, though you can still access it using API(default value: `True`).

Further documentation is available at instamojo.com/developers/request-a-payment-api/