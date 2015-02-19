import unittest
from dl_number_validation import (
    STATE_FORMATS, OTHER_STATES, is_valid)


class DLNumberValidationTest(unittest.TestCase):

    def test_invalid_dl_number_all(self):
        """
        Invalid formats for every state.
        """
        for dl_state in STATE_FORMATS.keys():
            self.assertFalse(is_valid('!@#$%^&*()', dl_state))
            self.assertFalse(is_valid(
                'reallyreallyreallylooooooonyyyalphastring',
                dl_state))
            self.assertFalse(is_valid(
                '00000001111111112222222222222222222222222',
                dl_state))
            self.assertFalse(is_valid('a012345678901234', dl_state))
            self.assertFalse(is_valid('', dl_state))
            self.assertFalse(is_valid('-', dl_state))
            self.assertFalse(is_valid('*', dl_state))
            self.assertFalse(is_valid('+', dl_state))
            self.assertFalse(is_valid('#', dl_state))
            self.assertFalse(is_valid('&', dl_state))
            self.assertFalse(is_valid('~', dl_state))
            self.assertFalse(is_valid('123~4567', dl_state))
            self.assertFalse(is_valid('@', dl_state))
            self.assertFalse(is_valid('abcd', dl_state))
            self.assertFalse(is_valid('1234a67890b2', dl_state))

    def test_alabama(self):
        dl_state = 'AL'
        self.assertTrue(is_valid('1', dl_state))
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_alaska(self):
        dl_state = 'AK'
        self.assertTrue(is_valid('1', dl_state))
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_arizona(self):
        dl_state = 'AZ'
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a123456', dl_state))
        self.assertTrue(is_valid('A123456', dl_state))
        self.assertTrue(is_valid('aB12345', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))

    def test_arkansas(self):
        dl_state = 'AR'
        self.assertTrue(is_valid('1234', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_california(self):
        dl_state = 'CA'
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a1234567', dl_state))
        self.assertTrue(is_valid('A1234567', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_colorado(self):
        dl_state = 'CO'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('a123456', dl_state))
        self.assertTrue(is_valid('A123456', dl_state))
        self.assertTrue(is_valid('Ab12345', dl_state))

    def test_connecticut(self):
        dl_state = 'CT'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_delaware(self):
        dl_state = 'DE'
        self.assertTrue(is_valid('1', dl_state))
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_dc(self):
        dl_state = 'DC'
        self.assertFalse(is_valid('1234', dl_state))
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_florida(self):
        dl_state = 'FL'
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a123456789012', dl_state))
        self.assertTrue(is_valid('C123456789012', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_georgia(self):
        dl_state = 'GA'
        self.assertFalse(is_valid('12345', dl_state))
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_hawaii(self):
        dl_state = 'HI'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('M12345678', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_idaho(self):
        dl_state = 'ID'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('ab123456a', dl_state))
        self.assertTrue(is_valid('AB123456A', dl_state))

    def test_illinois(self):
        dl_state = 'IL'
        self.assertFalse(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678901', dl_state))
        self.assertTrue(is_valid('A123456789012', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_indiana(self):
        dl_state = 'IN'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a123456789', dl_state))
        self.assertTrue(is_valid('A123456789', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_iowa(self):
        dl_state = 'IA'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a12345678', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))
        self.assertTrue(is_valid('123ab1234', 'IA'))
        self.assertTrue(is_valid('123AB1234', 'IA'))

    def test_kansas(self):
        dl_state = 'KS'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('A12345678', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))
        self.assertTrue(is_valid('a1a1a', dl_state))
        self.assertTrue(is_valid('A1a1C', dl_state))

    def test_kentucky(self):
        dl_state = 'KY'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('A12345678', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_louisiana(self):
        dl_state = 'LA'
        self.assertTrue(is_valid('1234', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_maine(self):
        dl_state = 'ME'
        self.assertFalse(is_valid('1234', dl_state))
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('1234567a', dl_state))
        self.assertTrue(is_valid('1234567A', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))

    def test_maryland(self):
        dl_state = 'MD'
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a123456789012', dl_state))
        self.assertTrue(is_valid('M123456789012', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_massachusetts(self):
        dl_state = 'MA'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('A12345678', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_michigan(self):
        dl_state = 'MI'
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a123456789012', dl_state))
        self.assertTrue(is_valid('L123456789012', dl_state))
        self.assertTrue(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_minnesota(self):
        dl_state = 'MN'
        self.assertFalse(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a123456789012', dl_state))
        self.assertTrue(is_valid('M123456789012', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_mississippi(self):
        dl_state = 'MS'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456789012', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_missouri(self):
        dl_state = 'MO'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('a123456r', dl_state))
        self.assertTrue(is_valid('12345678ab', dl_state))
        self.assertTrue(is_valid('123456789a', dl_state))

        self.assertTrue(is_valid('A12345678', dl_state))
        self.assertTrue(is_valid('A123456R', dl_state))
        self.assertTrue(is_valid('12345678AB', dl_state))
        self.assertTrue(is_valid('123456789A', dl_state))

        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_montana(self):
        dl_state = 'MT'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('1234567890123', dl_state))
        self.assertTrue(is_valid('a12345678', dl_state))
        self.assertTrue(is_valid('A12345678', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_nebraska(self):
        dl_state = 'NE'
        self.assertTrue(is_valid('1234', dl_state))
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('12345678', dl_state))

    def test_nevada(self):
        dl_state = 'NV'
        self.assertFalse(is_valid('1234', dl_state))
        self.assertTrue(is_valid('1234567890', dl_state))
        self.assertTrue(is_valid('x12345678', dl_state))
        self.assertTrue(is_valid('X12345678', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('a12345678', dl_state))
        self.assertFalse(is_valid('12345678', dl_state))

    def test_new_hampshire(self):
        dl_state = 'NH'
        self.assertFalse(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a12345', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))
        self.assertTrue(is_valid('12abc12345', dl_state))
        self.assertTrue(is_valid('12ABC12345', dl_state))

    def test_new_jersey(self):
        dl_state = 'NJ'
        self.assertFalse(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a12345678901234', dl_state))
        self.assertTrue(is_valid('N12345678901234', dl_state))
        self.assertFalse(is_valid('a1234567890', dl_state))
        self.assertFalse(is_valid('ab1234567', dl_state))

    def test_new_mexico(self):
        dl_state = 'NM'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('123456', dl_state))

    def test_new_york(self):
        dl_state = 'NY'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('1234567890123456', dl_state))
        self.assertTrue(is_valid('a1234567', dl_state))
        self.assertTrue(is_valid('A123456789012345678', dl_state))
        self.assertTrue(is_valid('abcdefgh', dl_state))
        self.assertTrue(is_valid('NEWaYORK', dl_state))
        self.assertFalse(is_valid('123456', dl_state))

    def test_north_carolina(self):
        dl_state = 'NC'
        self.assertTrue(is_valid('123', dl_state))
        self.assertTrue(is_valid('123456789012', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_north_dakota(self):
        dl_state = 'ND'
        self.assertFalse(is_valid('123', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))
        self.assertTrue(is_valid('abc123456', dl_state))
        self.assertTrue(is_valid('NDc123456', dl_state))

    def test_ohio(self):
        dl_state = 'OH'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('ab123', dl_state))
        self.assertTrue(is_valid('a123456', dl_state))
        self.assertTrue(is_valid('OH123', dl_state))
        self.assertTrue(is_valid('AB23456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_oklahoma(self):
        dl_state = 'OK'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertTrue(is_valid('a123456789', dl_state))
        self.assertTrue(is_valid('O123456789', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_oregon(self):
        dl_state = 'OR'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('ab12345', dl_state))
        self.assertTrue(is_valid('OR12345', dl_state))
        self.assertTrue(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_pennsylvania(self):
        dl_state = 'PA'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('123456789', dl_state))

    def test_rhode_island(self):
        dl_state = 'RI'
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertTrue(is_valid('a123456', dl_state))
        self.assertTrue(is_valid('R123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_south_carolina(self):
        dl_state = 'SC'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('12345678901', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_south_dakota(self):
        dl_state = 'SD'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertFalse(is_valid('12345678901', dl_state))
        self.assertTrue(is_valid('123456789012', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_tennessee(self):
        dl_state = 'TN'
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_texas(self):
        dl_state = 'TX'
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_utah(self):
        dl_state = 'UT'
        self.assertTrue(is_valid('1234', dl_state))
        self.assertTrue(is_valid('1234567890', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_vermont(self):
        dl_state = 'VT'
        self.assertTrue(is_valid('12345678', dl_state))
        self.assertTrue(is_valid('1234567a', dl_state))
        self.assertTrue(is_valid('1234567A', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_virginia(self):
        dl_state = 'VA'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('a1234567890', dl_state))
        self.assertTrue(is_valid('V1234567890', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_washington(self):
        dl_state = 'WA'
        self.assertTrue(is_valid('abcd12345678', dl_state))
        self.assertTrue(is_valid('ab**********', dl_state))
        self.assertTrue(is_valid('WASH12345678', dl_state))
        self.assertTrue(is_valid('ab*INGTON***', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('abcd123456789', dl_state))

    def test_west_virginia(self):
        dl_state = 'WV'
        self.assertTrue(is_valid('1234567', dl_state))
        self.assertTrue(is_valid('a12345', dl_state))
        self.assertTrue(is_valid('WV123456', dl_state))
        self.assertFalse(is_valid('a1234567', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_wisconsin(self):
        dl_state = 'WI'
        self.assertTrue(is_valid('a1234567890123', dl_state))
        self.assertTrue(is_valid('W1234567890123', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))

    def test_wyoming(self):
        dl_state = 'WY'
        self.assertTrue(is_valid('123456789', dl_state))
        self.assertTrue(is_valid('1234567890', dl_state))
        self.assertFalse(is_valid('ab123', dl_state))
        self.assertFalse(is_valid('a123456', dl_state))
        self.assertFalse(is_valid('1234567890123', dl_state))
        self.assertFalse(is_valid('icantbelieveijustwroteallthesetests',
                                  dl_state))

    def test_territories(self):
        for dl_state in OTHER_STATES:
            self.assertTrue(is_valid('1234567890', dl_state, True))
            self.assertTrue(is_valid('ab123', dl_state, True))
            self.assertTrue(is_valid('**--  ', dl_state, True))
            self.assertTrue(is_valid('.', dl_state, True))
            self.assertTrue(is_valid('icantbelieveijustwroteallthesetests',
                                     dl_state, True))

    def test_invalid_state(self):
        """
        Invalid states should raise an exception
        """
        dl_num = "doesnt_matter"
        self.assertRaises(Exception, is_valid, dl_num, "fakestate")
        self.assertRaises(Exception, is_valid, dl_num, "ZZ")
        self.assertRaises(Exception, is_valid, dl_num, "california")

    def test_allow_territories(self):
        dl_num = "doesnt_matter"
        self.assertRaises(Exception, is_valid, dl_num, "AS", False)
        self.assertRaises(Exception, is_valid, dl_num, "FM", False)
        self.assertRaises(Exception, is_valid, dl_num, "AA", False)
        self.assertTrue(is_valid(dl_num, "AS", True))
        self.assertTrue(is_valid(dl_num, "FM", True))
        self.assertTrue(is_valid(dl_num, "AA", True))

if __name__ == '__main__':
    unittest.main()
