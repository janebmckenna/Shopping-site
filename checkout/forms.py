from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',  
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'county',
                  'country',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name' : 'Full Name',
            'email' : 'Email Address',
            'phone_number' : 'Phone Number',
            'street_address1' : 'Street Address', 
            'street_address2' : 'Street Address',
            'town_or_city' : 'Town or City', 
            'postcode' : 'Postal Code', 
            'county' : 'County or State',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-layout'
            self.fields[field].label = False