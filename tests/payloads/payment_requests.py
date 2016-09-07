payment_requests_payload = {
    'payment_request_create': {
        'request': {
            'purpose': 'FIFA 16',
            'amount': '2500',
            'buyer_name': 'Jon Snow',
            'email': 'jon+snow@mailinator.com',
            'phone': '+919999999990',
            'send_email': True,
            'send_sms': True,
            'redirect_url': 'https://www.instamojo.com/redirect-handler',
            'webhook': 'https://www.instamojo.com/webhook-handler',
            'allow_repeated_payments': 'allow_repeated_payments'
        }
    },
    'payment_request_status': {
        'request': {
            'id': '92e58bd771414d05a5e443b0a85f8b43'
        }
    },
    'payment_requests_list': {
        'request': {}
    },
    'payment_requests_list_optional_params': {
        'request': {
            'min_created_at': '2016-08-10T13:23:20Z',
            'max_created_at': '2016-08-12T13:23:20Z',
            'min_modified_at': '2016-08-10T13:23:20Z',
            'max_modified_at': '2016-08-12T13:23:20Z'
        }
    },
    'payment_request_payment_status': {
        'request': {
            'id': '92e58bd771414d05a5e443b0a85f8b43',
            'payment_id': 'MOJO5a06005J21512197'
        }
    }
}
