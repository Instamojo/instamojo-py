## Refunds

### Create a new Refund

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Refund
    response = api.refund_create(
        payment_id='MOJO5c04000J30502939',
        type="QFL",
        body="Customer is not satisfied.")

    # print the unique ID(or Refund ID)
    print response['refund']['id']
    # print the status
    print response['refund']['status']

### Get the details of a Refund

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Payment Request
    response = api.refund_detail('[REFUND ID]')

    print response['refund']['status']  # Get the status


### Get a list of all Refunds

    from instamojo import Instamojo
    api = Instamojo(api_key='[API_KEY]',
                    auth_token='[AUTH_TOKEN]')

    # Create a new Payment Request
    response = api.refunds_list()

    # Loop over all of the Refunds and print their status
    for refund in response['refunds']:
        print refund['status']

## Available Refund Functions

 * `refund_create(payment_id, type, body)` => Refund
 * `refund_detail(id)` => Refund
 * `refunds_list()` => List of Refunds

## Refund Creation Parameters

### Required
  * `payment_id`: Payment ID for which Refund is being requested.
  * `type`: A three letter short-code to identify the type of the refund. Check the
            REST docs for more info on the allowed values.
  * `body`: Additional explanation related to why this refund is being requested.

### Optional
  * `refund_amount`: This field can be used to specify the refund amount. For instance, you
            may want to issue a refund for an amount lesser than what was paid. If
            this field is not provided then the total transaction amount is going to
            be used.

Further documentation is available at https://www.instamojo.com/developers/rest/#toc-refunds