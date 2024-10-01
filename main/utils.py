from django.utils import formats

def format_price(value):
    if value is None:
        return ""
    # Ensure the value is a float
    value = float(value)
    # Format the price with two decimal places
    formatted_price = f"{value:,.2f}"
    # Replace commas with periods and the decimal point with a comma
    return formatted_price.replace(',', '.').replace('.', ',', 1)