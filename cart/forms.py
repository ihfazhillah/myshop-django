from django import forms
from django.utils.translation import gettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field, Fieldset, ButtonHolder,HTML, Submit
from crispy_forms.bootstrap import FieldWithButtons, StrictButton

update = _('Update')
add_to_cart = _('Add to cart')


class CartAddForm(forms.Form):

    quantity = forms.IntegerField(min_value=1, label='')
    update = forms.CharField(required=False,
                             initial=False,
                             widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)
        super(CartAddForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        if is_update:
            self.helper.layout = Layout(
                    Field('update', type='hidden'),
                    FieldWithButtons('quantity', Submit(name='submit', value=update,css_class='btn-primary'), css_class='md-form'),
                )
        else:
            self.helper.layout = Layout(
                    Field('update', type='hidden'),
                    FieldWithButtons('quantity', HTML('''<button class="btn btn-primary" type="submit">{submit_text}
                                                                      <i class="fa fa-shopping-cart ml-1"></i>
                                                                    </button>
                                                      '''.format(submit_text=add_to_cart)), css_class='md-form'),
                )


