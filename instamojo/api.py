class API:
    token = None

    def __init__(self, token=None):
        self.token = token

    def auth(self, username, password):
        raise NotImplementedError('Whoops!')

    def offer_list(self):
        raise NotImplementedError('Dang!')

    def offer_detail(self, slug):
        raise NotImplementedError('Shite!')

    def offer_create(self, title, description=None, # Basic
                     base_price=None, currency=None, # Pricing
                     quantity=None, # Quantity
                     start_date=None, end_date=None, venue=None, timezone=None, # Event
                     redirect_url=None, # Redirect user to URL after successful payment
                     note=None, # Show note, embed in receipt after successful payment
                     upload_file=None, # File to upload
                     cover_image=None, # Cover image to associate with offer
                     ):
        raise NotImplementedError('Yikes!')

    def offer_edit(self, slug, # Need slug to identify offer
                     title=None, description=None, # Basic
                     base_price=None, currency=None, # Pricing
                     quantity=None, # Quantity
                     start_date=None, end_date=None, venue=None, timezone=None, # Event
                     redirect_url=None, # Redirect user to URL after successful payment
                     note=None, # Show note, embed in receipt after successful payment
                     upload_file=None, # File to upload
                     cover_image=None, # Cover image to associate with offer
                     ):
        raise NotImplementedError('Uh oh!')

    def offer_delete(self, slug):
        raise NotImplementedError('Shucks!')


    def _api_call(self, method, path, **kwargs):
        raise NotImplementedError('Aw crap!')
