def validate(values):
    is_valid = True
    values_invalid = []

    if len(values['-FIRSTNAME-']) == 0:
        values_invalid.append('first_name')
        is_valid = False

    if len(values['-LASTNAME-']) == 0:
        values_invalid.append('last_name')
        is_valid = False

    if len(values['-STREETADDRESS-']) == 0:
        values_invalid.append('Street_address')
        is_valid = False

    if len(values['-ZIPCODE-']) == 0:
            values_invalid.append('zip_code')
            is_valid = False

    if len(values['-MAIL-']) == 0:
            values_invalid.append('mail')
            is_valid = False

    if len(values['-PAYEDFEE-']) == 0:
            values_invalid.append('payed_fee')
            is_valid = False

    result = {"is_valid": is_valid, "values_invalid": values_invalid}
    return result


def generate_error_message(values_invalid):
    error_message = ''
    for value_invalid in values_invalid:
        error_message += ('\nInvalid' + ':' + value_invalid)

    return