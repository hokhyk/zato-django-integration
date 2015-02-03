
from django.forms import CharField, ChoiceField, Form, Select, TextInput

class GetCustomerForm(Form):
    cust_id = CharField(widget=TextInput())
    client_type = ChoiceField()

    def __init__(self, *args, **kwargs):
        super(GetCustomerForm, self).__init__(*args, **kwargs)

        self.fields['client_type'].choices = [
            ['AnyServiceInvoker', 'AnyServiceInvoker'],
            ['JSONClient', 'JSONClient']
        ]
