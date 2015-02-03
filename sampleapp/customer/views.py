# -*- coding: utf-8 -*-

# stdlib
from datetime import datetime

# Django
from django.template.response import TemplateResponse

def home(req):

    # The data provided on input
    cust_id = req.GET.get('cust_id')

    if cust_id:

        before = datetime.utcnow()

        # Invoke an echo service with the user-provided input.
        response = req.zato_client.invoke('customer.get', {'cust_id':cust_id})

        # How long we waited for Zato, in milliseconds
        time = (datetime.utcnow() - before).total_seconds() * 1000

    else:
        time, response = None, None

    print(response)

    return TemplateResponse(req, 'customer.html',
        {'time': time, 'cust_id':cust_id, 'response':response})
