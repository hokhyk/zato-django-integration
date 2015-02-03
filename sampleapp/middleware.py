# -*- coding: utf-8 -*-

# Zato
from zato.client import AnyServiceInvoker, JSONClient

# Our app
from settings import CLIENT_ADDRESS, CLIENT_CREDENTIALS, CLIENT_PATH_ANY, CLIENT_PATH_JSON

class ZatoMiddleware(object):
    def process_request(self, req):
        req.client_any = AnyServiceInvoker(CLIENT_ADDRESS, CLIENT_PATH_ANY, CLIENT_CREDENTIALS)
        req.client_json = JSONClient(CLIENT_ADDRESS, CLIENT_PATH_JSON, CLIENT_CREDENTIALS)

