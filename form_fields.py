from django import forms
from decimal import Decimal
from django.conf import settings


class AmountFormField(forms.DecimalField):
    def __init__(self, *args, **kwargs):
        # Get the price unit from the kwargs
        price_unit = settings.AMOUNT_FIELD.get('price_unit')

        # Call the parent class's __init__ method
        super().__init__(*args, **kwargs)
        
        # Add the price unit to the label
        if price_unit:
            self.label = f"{self.label} ({price_unit})"

    def to_python(self, value):
        if value is not None:
            if not value:
                raise forms.ValidationError("This field is required.")

            try:

                # Replace commas and convert to float
                print(value)
                value = Decimal(str(value).replace(',', ''))
                print(value)
            except ValueError:
                raise forms.ValidationError("Enter a valid number.")
        return value

