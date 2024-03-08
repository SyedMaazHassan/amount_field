# amount_field

`amount_field` is a Django app designed to facilitate projects dealing with amounts, currencies, and prices. It provides custom Django model and form fields for handling amounts, along with functionality to format currency with commas for thousands and add commas while typing currency in inputs.

## Features

- **AmountField**: A custom Django model field for storing amounts.
- **AmountFormField**: A custom Django form field for handling amounts in forms.
- **Custom template tag**: Provides a custom template tag for formatting currency with commas for thousands.
- **Real-time formatting**: Automatically adds commas while typing currency in inputs.

## Installation

You can install `amount_field` via pip:

```bash
pip install amount-field
```

## Usage

1. **Model Field**:
   ```python
   from django.db import models
   from amount_field.models import AmountField

   class YourModel(models.Model):
       amount = AmountField()
   ```

2. **Form Field**:
   ```python
   from django import forms
   from amount_field.forms import AmountFormField

   class YourForm(forms.Form):
       amount = AmountFormField()
   ```

3. **Template Tag**:
   ```django
   {% load amount_tags %}
   {{ amount_value|format_currency }}
   ```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE.txt).

Feel free to copy and paste this content into your README.md file and make any necessary adjustments. Let me know if you need further assistance!
