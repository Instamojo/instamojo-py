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
    for link in response['links']
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

Further documentation is available at https://www.instamojo.com/api/1.1/docs/
