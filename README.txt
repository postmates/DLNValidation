=============
DLNValidation
=============

A python library for validation of USA drivers license numbers.
Dl-number-validation validates if a drivers license is a valid format for the two letter postal code for the state.

Formats are mostly defined by http://adr-inc.com/PDFs/State_DLFormats.pdf. We've added in a couple more formats for drivers license's that we've found valid based on real drivers license numbers.

Installation
============
`pip install DLNValidation`

Usage
=====
Typical usage often looks like this::

    from dlnvalidation import is_valid

    if is_valid('C1234567', 'CA'):
        print "Your drivers license number is valid! Yay!"

If you want US territories to be used for validation call `is_valid` with `allow_territories=True`. Be warned, currently these additional territories accept any format of drivers license.
