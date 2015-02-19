import re


# In alphabetical order by state, not by abbreviation
STATE_FORMATS = {
    'AL': r'[0-9]{1,7}$',
    'AK': r'[0-9]{1,7}$',
    'AZ': r'[a-z][0-9]{1,8}$|[a-z]{2}[0-9]{2,5}$|[0-9]{9}$',
    'AR': r'[0-9]{4,9}$',
    'CA': r'[a-z][0-9]{7}$',
    'CO': r'[0-9]{9}$|[a-z][0-9]{3,6}$|[a-z]{2}[0-9]{2,5}$',
    'CT': r'[0-9]{9}$',
    'DE': r'[0-9]{1,7}$',
    'DC': r'[0-9]{7}$|[0-9]{9}$',
    'FL': r'[a-z][0-9]{12}$',
    'GA': r'[0-9]{7,9}$',
    'HI': r'[a-z][0-9]{8}$|[0-9]{9}$',
    'ID': r'[a-z]{2}[0-9]{6}[a-z]$|[0-9]{9}$',
    'IL': r'[a-z][0-9]{11,12}$',
    'IN': r'[a-z][0-9]{9}$|[0-9]{9,10}$',
    'IA': r'[0-9]{9}$|[0-9]{3}[a-z]{2}[0-9]{4}$',
    'KS': r'[a-z][0-9][a-z][0-9][a-z]|[a-z][0-9]{8}$|[0-9]{9}$',
    'KY': r'[a-z][0-9]{8,9}$|[0-9]{9}$',
    'LA': r'[0-9]{1,9}$',
    'ME': r'[0-9]{7,8}$|[0-9]{7}[a-z]$',
    'MD': r'[a-z][0-9]{12}$',
    'MA': r'[a-z][0-9]{8}$|[0-9]{9}$',
    'MI': r'[a-z]([0-9]{10}|[0-9]{12})$',
    'MN': r'[a-z][0-9]{12}$',
    'MS': r'[0-9]{9}$',
    'MO': r'[a-z][0-9]{5,9}$|[a-z][0-9]{6}r$|[0-9]{8}[a-z]{2}$|[0-9]{9}[a-z]$|[0-9]{9}$',
    'MT': r'[a-z][0-9]{8}$|[0-9]{13,14}$|[0-9]{9}$',
    'NE': r'[0-9]{1,7}$',
    'NV': r'[0-9]{9,10}$|[0-9]{12}$|x[0-9]{8}$',
    'NH': r'[0-9]{2}[a-z]{3}[0-9]{5}$',
    'NJ': r'[a-z][0-9]{14}$',
    'NM': r'[0-9]{8,9}$',
    'NY': r'[a-z]([0-9]{7}|[0-9]{18})$|[0-9]{8,9}$|[0-9]{16}$|[a-z]{8}$',
    'NC': r'[0-9]{1,12}$',
    'ND': r'[a-z]{3}[0-9]{6}$|[0-9]{9}$',
    'OH': r'[a-z][0-9]{4,8}$|[a-z]{2}[0-9]{3,7}$|[0-9]{8}$',
    'OK': r'[a-z][0-9]{9}$|[0-9]{9}$',
    'OR': r'[0-9]{1,9}$|[a-z][0-9]{6}$|[a-z]{2}[0-9]{5}$',
    'PA': r'[0-9]{8}$',
    'RI': r'[0-9]{7}$|[a-z][0-9]{6}$',
    'SC': r'[0-9]{5,11}$',
    'SD': r'[0-9]{6,10}$|[0-9]{12}$',
    'TN': r'[0-9]{7,9}$',
    'TX': r'[0-9]{7,8}$',
    'UT': r'[0-9]{4,10}$',
    'VT': r'[0-9]{8}$|[0-9]{7}a$',
    'VA': r'[a-z][0-9]{9,11}$|[0-9]{9}$',
    'WA': r'[a-z][a-z0-9*]{11}$',
    'WV': r'[0-9]{7}$|[a-z]{1,2}[0-9]{5,6}$',
    'WI': r'[a-z][0-9]{13}$',
    'WY': r'[0-9]{9,10}$'
}


OTHER_STATES = [
    # Territorries
    'AS', 'GU', 'MP', 'PR', 'VI', 'UM',

    # Freely Associated States
    'FM', 'MH', 'PW',

    # Armed Forces
    'AA', 'AE', 'AP'
]


def is_valid(dl_number, dl_state, allow_territories=False):
    """
    dl_number is a drivers license number string.
    dl_state is the state abbreviation of the state of the drivers license.
    if allow_territories is set, all drivers licenses for territorries,
    freely associated states and armed forces will be processed as valid.
    If not set, they will be considered an invalid state and an exception
    will be thrown.
    Returns True if given a valid drivers license number.

    All drivers license numbers must be alphanumeric and conform to
    specific state formats.
    For more info, see http://adr-inc.com/PDFs/State_DLFormats.pdf.
    """

    if not dl_number:
        return False

    if dl_state in STATE_FORMATS:
        regex = STATE_FORMATS[dl_state]
        is_valid = bool(re.match(regex, dl_number, re.IGNORECASE))
        return is_valid
    elif allow_territories and dl_state in OTHER_STATES:
        return True
    else:
        raise Exception("Invalid state for drivers license number validation!")
