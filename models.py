from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from .form_fields import AmountFormField

class AmountField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        """
        Initialize the AmountField with default values for max_digits and decimal_places.
        """
        kwargs.setdefault('max_digits', 10)
        kwargs.setdefault('decimal_places', 2)
        super().__init__(*args, **kwargs)

    def _convert_to_decimal(self, value):
        """
        Convert the input value to a Decimal object, handling commas.
        """
        if value is not None:
            try:
                value = Decimal(str(value).replace(',', ''))
            except ValueError as e:
                raise ValidationError(f"Invalid value: {e}")
        return value

    def to_python(self, value):
        """
        Convert the input value to a Decimal object, handling commas.
        """
        return self._convert_to_decimal(value)

    def from_db_value(self, value, expression, connection):
        """
        Convert the value from the database to a Decimal object.
        """
        return self._convert_to_decimal(value)

    def get_prep_value(self, value):
        """
        Convert the value to a Decimal object, handling commas.
        """
        return self._convert_to_decimal(value)

    def formfield(self, **kwargs):
        """
        Customize the form field for the AmountField.
        """
        defaults = {'form_class': AmountFormField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

    def format_value(self):
        """
        Format the amount value with commas and two decimal places.
        """
        if not self.value:
            return None

        # Convert the value to Decimal
        number = Decimal(self.value)

        # Format the number with commas and two decimal places
        formatted_text = "{:,.2f}".format(number)

        # Remove decimal if .00
        formatted_text = formatted_text.rstrip('0').rstrip('.')

        return formatted_text

    @property
    def display(self):
        """
        Return a formatted representation of the AmountField value.
        """
        # Call the format_value method to get the formatted value
        return self.format_value()
