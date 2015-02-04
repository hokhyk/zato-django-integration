# -*- coding: utf-8 -*-

# stdlib
from datetime import datetime

# Django
from django.template.response import TemplateResponse

# Our app
from customer.forms import GetCustomerForm

def home(req):

    form = GetCustomerForm(req.GET)

    # The data provided on input
    cust_id = req.GET.get('cust_id')
    client_type = req.GET.get('client_type')

    if cust_id:

        # What to invoke the service with
        request = {'cust_id':cust_id}

        # When was the service invoked
        before = datetime.utcnow()

        # Invoke the service with the user-provided input using a selected client
        if client_type == 'AnyServiceInvoker':
            response = req.client_any.invoke('customer.get1', request)
        else:
            response = req.client_json.invoke(request)

        # How long we waited for the response, in milliseconds
        time = (datetime.utcnow() - before).total_seconds() * 1000

    else:
        time, response = None, None

    return TemplateResponse(req, 'customer.html',
        {'time':time, 'form':form, 'response':response})
