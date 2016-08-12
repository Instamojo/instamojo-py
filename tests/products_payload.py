products_payload = {
    'basic_product_creation': {
        'request': {
            'currency': 'INR',
            'base_price': '50.00',
            'description': 'This is an example product.',
            'title': 'Hello API'
        }
    },
    'event_product_creation': {
        'request': {
            'currency': 'INR',
            'base_price': '50.00',
            'description': 'This is an example product.',
            'title': 'Hello API',
            'start_date': '2016-08-03 16:30',
            'end_date': '2016-08-04 18:14',
            'venue': 'A galaxy far, far away',
            'timezone': 'Asia/Kolkata'
        }
    },
    'digital_product_creation': {
        'request': {
            'currency': 'INR',
            'base_price': '50.00',
            'description': 'This is an example product.',
            'title': 'Hello API',
            'file_upload': '/Users/DarthVader/Padme.jpg'
        }
    },
    'product_creation_with_cover_image': {
        'request': {
            'currency': 'INR',
            'base_price': '50.00',
            'description': 'This is an example product.',
            'title': 'Hello API',
            'cover_image': '/Users/DarthVader/Padme.jpg'
        }
    },
    'product_creation_with_all_params': {
        'request': {
            'currency': 'INR',
            'base_price': '50.00',
            'description': 'This is an example product.',
            'title': 'Hello API',
            'quantity': 100,
            'start_date': '2016-08-03 16:30',
            'end_date': '2016-08-04 18:14',
            'venue': 'A galaxy far, far away',
            'timezone': 'Asia/Kolkata',
            'redirect_url': 'https://www.instamojo.com/redirect_handler',
            'webhook_url': 'https://www.instamojo.com/webhook_handler',
            'note': 'Thanks for buying things.',
            'enable_pwyw': True,
            'enable_sign': True,
            'socialpay_platforms': 'twitter',
            'file_upload': '/Users/DarthVader/Padme.jpg',
            'cover_image': '/Users/DarthVader/Padme.jpg'
        }
    },
    'product_edit_with_all_params': {
        'request': {
            'slug': 'hello-api',
            'currency': 'INR',
            'base_price': '50.00',
            'description': 'This is an example product.',
            'title': 'Hello API',
            'quantity': 100,
            'start_date': '2016-08-03 16:30',
            'end_date': '2016-08-04 18:14',
            'venue': 'A galaxy far, far away',
            'timezone': 'Asia/Kolkata',
            'redirect_url': 'https://www.instamojo.com/redirect_handler',
            'webhook_url': 'https://www.instamojo.com/webhook_handler',
            'note': 'Thanks for buying things.',
            'enable_pwyw': True,
            'enable_sign': True,
            'socialpay_platforms': 'twitter',
            'file_upload': '/Users/DarthVader/Padme.jpg',
            'cover_image': '/Users/DarthVader/Padme.jpg'
        }
    },
    'product_delete': {
        'request': {
            'slug': 'hello-api'
        }
    },
    'product_details': {
        'request': {
            'slug': 'hello-api'
        }
    },
    'products_list': {
        'request': {}
    }
}