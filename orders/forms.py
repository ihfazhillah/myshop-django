from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field, Fieldset, ButtonHolder,HTML, Submit, Div, Row
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from .models import Order


class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                'first_name', 'last_name', 'email', 'address', 'postal_code', 'city',
                class_name='md-form'
            ),
            HTML('<hr class="mb-4">'),
            Submit(name='create-order', value='Create Order', class_name='btn btn-block btn-primary btn-lg')
        )


    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

