# -*- coding: UTF-8 -*-

import json

from six.moves import urllib as urllib
from yelp.errors import ErrorHandler

API_HOST = 'api.yelp.com'
BUSINESS_SEARCH_PATH = '/v3/businesses/search'

class Client(object):

    def __init__(self, access_token):
        self.access_token = access_token
        self._error_handler = ErrorHandler()

    def business_search(self, **url_params):
        return self._make_request(
            path = BUSINESS_SEARCH_PATH,
            url_params = dict(**url_params)
        )

    def _make_request(self, path, url_params={}):

        url = 'https://{0}{1}?'.format(
            API_HOST,
            urllib.parse.quote(path.encode('utf-8'))
        ) + urllib.parse.urlencode(url_params)

        request = urllib.request.Request(
            url,
            headers = {
                "Authorization": "Bearer {0}".format(self.access_token)
            }
        )

        try:
            conn = urllib.request.urlopen(request)
        except urllib.error.HTTPError as error:
            self._error_handler.raise_error(error)

        try:
            response = json.loads(conn.read().decode('utf-8'))
        finally:
            conn.close()

        return response


