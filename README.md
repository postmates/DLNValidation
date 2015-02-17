dl-number-validation - A python library for validation of USA drivers license numbers
=========================
Validates if a drivers license is a valid format for a given two letter state abbreviation according to http://adr-inc.com/PDFs/State_DLFormats.pdf

Installation
------------
`pip install dl-number-validation`

Usage
-----
```
from dl-number-validation import is_valid

if is_valid('C1234567', 'CA'):
    print "Your drivers license number is valid! Yay!"
```
