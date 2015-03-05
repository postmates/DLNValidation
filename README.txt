=============
DLNValidation
=============

A python library for validation of USA drivers license numbers.
Dl-number-validation validates if a drivers license is a valid format for the two letter postal code for the state.

Formats are defined by http://www.deverusdemos.com/Help/FlashHelp/Search_Types/Formats_for_MVR_license_numbers.htm

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
