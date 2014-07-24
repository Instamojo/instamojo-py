# Instamojo API

Assists you to programmatically create, edit and delete offers on Instamojo.

## Installation

If you download source, run `python setup.py install` or you can run
`pip install instamojo` to automatically download and install the library.


## Usage

    from instamojo import Instamojo
    api = Instamojo(api_key='email api@instamojo.com for api_key')
    token = api.auth(username='USERNAME', password='PASSWORD')

You should save this `token` somewhere for reusing in all subsequent calls.

    from instamojo import Instamojo
    api = Instamojo(api_key='email api@instamojo.com for api_key',
              token='token-you-got-from-auth-call')
    api.offer_list()

    print api.offer_create(title='Hello, world!', base_price=0, currency='INR')

This will give you JSON object containing details of the offer that was just created.

You have these functions to interact with the API:
 * `debug()`
 * `auth(username, password)`
 * `offer_create(title, base_price, currency)`
 * `offer_edit(slug)`
 * `offer_delete(slug)`

For `offer_create`, `title`, `base_price` and `currency` are the bare minimum
pieces of information that is required. You can (and should) as much relevant information
as possible.

 * `title` A brief title that describes the offer.
 * `base_price` Price at which you wish to sell the offer.
 * `currency` Currency in which you wish to sell the offer. Options: `INR` and `USD`
 * `description` A detailed description of the offer, markdown and embedding media links such as youtube, soundcloud, flickr is supported.
 * `quantity` If you wish to limit the number of sales (such as available seats for a workshop), set the limit here.
 * `start_date` If the offer is for an event, the date and time when the event begins.
 * `end_date` If the offer is for an event, the date and time when the event ends.
 * `venue` If the offer is for an event, the venue where the event will take place.
 * `timezone` If the offer is for an event, the timezone of the venue.
 * `redirect_url` You can redirect a user after successful payment to another URL (such as a survey or a custom thank you page).
 * `note` A message shown to user after successful payment, also included in their receipt.
 * `upload_file` Full path to the file you want to upload for selling.
 * `cover_image` Full path to a JPEG/PNG image that you want to use as cover image for the offer.
