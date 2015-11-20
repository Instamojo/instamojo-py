# Instamojo API

Assists you to programmatically create, edit and delete links on Instamojo.

## Installation

[Download the source code](https://github.com/Instamojo/instamojo-py/archive/master.zip),
run `python setup.py install` to install the library.

## Authentication Keys

You can find your API_KEY and AUTH_TOKEN at the API Documentation Page.
Create an account on Instamojo, log in and visit this link:
https://www.instamojo.com/api/1.1/docs/

## Usage

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Get a list of all Links that you have created and display their slugs.
    response = api.links_list()
    for link in response['links']:
        print link['slug']

    # Create a new Link
    response = api.link_create(title='Hello, world!',
                               description='Well, hello again.',
                               base_price=0,
                               currency='INR')

    # Display the URL of the newly created Link
    print response['link']

This will give you JSON object containing details of the link that was just created.

## Payments API and Webhook/Redirect

    from instamojo import Instamojo
    api = Instamojo(api_key, token_auth)
    payment = api.payment_detail(payment_id='PAYMENT ID YOU GOT FROM WEBHOOK OR REDIRECT')

This will return a Payment object with details of the transaction.

You have these functions to interact with the API:
 * `debug()`
 * `auth(username, password)`
 * `links_list()` => list of Links
 * `link_detail(slug)` => Link
 * `link_create(title, description, base_price, currency)` => Link
 * `link_edit(slug)` => Link
 * `link_delete(slug)` => No Data
 * `payments_list()` => List of Payments
 * `payment_detail(payment_id)` => Payment

## Link Creation Parameters

### Required

  * `title` - Title of the Link, be concise.
  * `description` - Describe what your customers will get, you can add terms and conditions and any other relevant information here. Markdown is supported, popular media URLs like Youtube, Flickr are auto-embedded.
  * `base_price` - Price of the Link. This may be 0, if you want to offer it for free.
  * `currency` - Currency options are `INR` and `USD`. Note that you need to have a Bank Account in USA to accept USD currencies.

### File and Cover Image
  * `file_upload` - Full path to the file you want to sell. This file will be available only after successful payment.
  * `cover_image` - Full path to the IMAGE you want to upload as a cover image.

### Quantity
  * `quantity` - Set to 0 for unlimited sales. If you set it to say 10, a total of 10 sales will be allowed after which the Link will be made unavailable.

### Post Purchase Note
  * `note` - A post-purchase note, will only displayed after successful payment. Will also be included in the ticket/ receipt that is sent as attachment to the email sent to buyer. This will not be shown if the payment fails.

### Event
  * `start_date` - Date-time when the event is beginning. Format: `YYYY-MM-DD HH:mm`
  * `end_date` - Date-time when the event is ending. Format: `YYYY-MM-DD HH:mm`
  * `venue` - Address of the place where the event will be held.
  * `timezone` - Timezone of the venue. Example: Asia/Kolkata

### Redirects and Webhooks
  * `redirect_url` - This can be a Thank-You page on your website. Buyers will be redirected to this page after successful payment.
  * `webhook_url` - Set this to a URL that can accept POST requests made by Instamojo server after successful payment.
  * `enable_pwyw` - set this to True, if you want to enable Pay What You Want. Default is False.
  * `enable_sign` - set this to True, if you want to enable Link Signing. Default is False. For more information regarding this, and to avail this feature write to support at instamojo.com.

Further documentation is available at https://www.instamojo.com/developers/


---

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
