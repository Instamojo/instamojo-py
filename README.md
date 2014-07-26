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
 * `links_list()` => list of Links
 * `link_detail(slug)` => Link
 * `link_create(title, description, base_price, currency)` => Link
 * `link_edit(slug)` => Link
 * `link_delete(slug)` => No Data
 * `payments_list()` => List of Payments
 * `payment_detail(payment_id)` => Payment

Further documentation is available at https://www.instamojo.com/api/1.1/docs/
