import re


# In alphabetical order by state, not by abbreviation
STATE_FORMATS = {
    'AL': r'[0-9]{1,7}$',
    'AK': r'[0-9]{1,7}$',
    'AZ': r'[a-zA-Z][0-9]{1,8}$|[a-zA-Z]{2}[0-9]{2,5}$|[0-9]{9}$',
    'AR': r'[0-9]{4,9}$',
    'CA': r'[a-zA-Z][0-9]{7}$',
    'CO': r'[0-9]{9}$|[a-zA-Z][0-9]{3,6}$|[a-zA-Z]{2}[0-9]{2,5}$',
    'CT': r'[0-9]{9}$',
    'DE': r'[0-9]{1,7}$',
    'DC': r'[0-9]{7}$|[0-9]{9}$',
    'FL': r'[a-zA-Z][0-9]{12}$',
    'GA': r'[0-9]{7,9}$',
    'HI': r'[a-zA-Z][0-9]{8}$|[0-9]{9}$',
    'ID': r'[a-zA-Z]{2}[0-9]{6}[a-zA-Z]$|[0-9]{9}$',
    'IL': r'[a-zA-Z][0-9]{11,12}$',
    'IN': r'[a-zA-Z][0-9]{9}$|[0-9]{9,10}$',
    'IA': r'[0-9]{9}$|[0-9]{3}[a-zA-Z]{2}[0-9]{4}$',
    'KS': r'[a-zA-Z][0-9][a-zA-Z][0-9][a-zA-Z]|[a-zA-Z][0-9]{8}$|[0-9]{9}$',
    'KY': r'[a-zA-Z][0-9]{8,9}$|[0-9]{9}$',
    'LA': r'[0-9]{1,9}$',
    'ME': r'[0-9]{7,8}$|[0-9]{7}[a-zA-Z]$',
    'MD': r'[a-zA-Z][0-9]{12}$',
    'MA': r'[a-zA-Z][0-9]{8}$|[0-9]{9}$',
    'MI': r'[a-zA-Z]([0-9]{10}|[0-9]{12})$',
    'MN': r'[a-zA-Z][0-9]{12}$',
    'MS': r'[0-9]{9}$',
    'MO': r'[a-zA-Z][0-9]{5,9}$|[a-zA-Z][0-9]{6}[rR]$|[0-9]{8}[a-zA-Z]{2}$|[0-9]{9}[a-zA-Z]$|[0-9]{9}$',
    'MT': r'[a-zA-Z][0-9]{8}$|[0-9]{13,14}$|[0-9]{9}$',
    'NE': r'[0-9]{1,7}$',
    'NV': r'[0-9]{9,10}$|[0-9]{12}$|[xX][0-9]{8}$',
    'NH': r'[0-9]{2}[a-zA-Z]{3}[0-9]{5}$',
    'NJ': r'[a-zA-Z][0-9]{14}$',
    'NM': r'[0-9]{8,9}$',
    'NY': r'[a-zA-Z]([0-9]{7}|[0-9]{18})$|[0-9]{8,9}$|[0-9]{16}$|[a-zA-Z]{8}$',
    'NC': r'[0-9]{1,12}$',
    'ND': r'[a-zA-Z]{3}[0-9]{6}$|[0-9]{9}$',
    'OH': r'[a-zA-Z][0-9]{4,8}$|[a-zA-Z]{2}[0-9]{3,7}$|[0-9]{8}$',
    'OK': r'[a-zA-Z][0-9]{9}$|[0-9]{9}$',
    'OR': r'[0-9]{1,9}$|[a-zA-Z][0-9]{6}$|[a-zA-Z]{2}[0-9]{5}$',
    'PA': r'[0-9]{8}$',
    'RI': r'[0-9]{7}$|[a-zA-Z][0-9]{6}$',
    'SC': r'[0-9]{5,11}$',
    'SD': r'[0-9]{6,10}$|[0-9]{12}$',
    'TN': r'[0-9]{7,9}$',
    'TX': r'[0-9]{7,8}$',
    'UT': r'[0-9]{4,10}$',
    'VT': r'[0-9]{8}$|[0-9]{7}[aA]$',
    'VA': r'[a-zA-Z][0-9]{9,11}$|[0-9]{9}$',
    'WA': r'[a-zA-Z]{1,7}',
    'WV': r'[0-9]{7}$|[a-zA-Z]{1,2}[0-9]{5,6}$',
    'WI': r'[a-zA-Z][0-9]{13}$',
    'WY': r'[0-9]{9,10}$'
}


def is_valid(dl_number, dl_state):
    """
    dl_number is a drivers license number string.
    dl_state is the state abbreviation of the state of the drivers license.
    Returns True if given a valid drivers license number.

    All drivers license numbers must be alphanumeric and conform to
    specific state formats.
    For more info, see http://adr-inc.com/PDFs/State_DLFormats.pdf.
    """

    if not dl_number:
        return False

    if dl_state in STATE_FORMATS:
        if dl_state == 'WA' and len(dl_number) != 12:
            # All drivers license from washington must be 12 characters
            return False
        regex = STATE_FORMATS[dl_state]
        is_valid = bool(re.match(regex, dl_number))
        return is_valid
    else:
        return bool(re.match(r'[a-zA-Z0-9]+$', dl_number))
