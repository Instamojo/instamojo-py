# Instamojo API

Assists you to programmatically create, edit and delete links on Instamojo.

## Installation

[Download the source code](https://github.com/Instamojo/instamojo-py/archive/master.zip),
run `python setup.py install` to install the library.


## Usage

    from instamojo import Instamojo
    api = Instamojo(api_key='email api@instamojo.com for api_key')
    token = api.auth(username='USERNAME', password='PASSWORD')

You should save this `token` somewhere for reusing in all subsequent calls.

    from instamojo import Instamojo
    api = Instamojo(api_key='email api@instamojo.com for api_key',
              token='token-you-got-from-auth-call')
    api.links_list()

    print api.link_create(title='Hello, world!', description='Well, hello again.', base_price=0, currency='INR')

This will give you JSON object containing details of the link that was just created.

## Payments API and Webhook/Redirect

    from instamojo import Instamojo
    api = Instamojo(api_key, token_auth)
    payment = api.payment_detail(payment_id='PAYMENT ID YOU GOT FROM WEBHOOK OR REDIRECT')

This will return a Payment object with details of the transaction.

You have these functions to interact with the API:
 * `debug()`
 * `auth(username, password)`
 * `links_list()`
 * `link_detail()`
 * `link_create(title, description, base_price, currency)`
 * `link_edit(slug)`
 * `link_delete(slug)`
 * `payments_list()`
 * `payment_detail()`


Further documentation is available at https://www.instamojo.com/api/1.1/docs/
