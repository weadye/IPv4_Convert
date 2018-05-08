import unittest
from ipv4_convertor import convert_ipv4


class convertorTest(unittest.TestCase):
    def test_success_1(self):
        self.assertEqual(convert_ipv4('172.168.5.1'), 2896692481, 'test fail')

    def test_success_2(self):
        self.assertEqual(convert_ipv4('192.168.1.1'), 3232235777, 'test fail')

    def test_success_3(self):
        self.assertEqual(convert_ipv4('0.0.0.0'), 0, 'test fail')

    def test_success_3(self):
        self.assertEqual(convert_ipv4('255.255.255.255'), 4294967295, 'test fail')

    def test_success_space_1(self):
        self.assertEqual(convert_ipv4('172. 168.5.1'), 2896692481, 'test fail')

    def test_success_space_2(self):
        self.assertEqual(convert_ipv4('172.168 . 5.1'), 2896692481, 'test fail')

    def test_success_space_3(self):
        self.assertEqual(convert_ipv4('172 .168 . 5 . 1'), 2896692481, 'test fail')

    def test_success_space_4(self):
        self.assertEqual(convert_ipv4('172.     168.5.1'), 2896692481, 'test fail')

    def test_success_space_5(self):
        self.assertEqual(convert_ipv4('172      .168.5.1'), 2896692481, 'test fail')

    def test_success_space_6(self):
        self.assertEqual(convert_ipv4('172      .          168.5.1'), 2896692481, 'test fail')

    def test_exception_wrong_spaces_1(self):
        self.assertRaisesRegexp(NameError, 'Error spaces', convert_ipv4, '17 2.168.5.1')

    def test_exception_wrong_spaces_2(self):
        self.assertRaisesRegexp(NameError, 'Error spaces', convert_ipv4, '17  2.168.5.1')

    def test_exception_null_address_number(self):
        self.assertRaisesRegexp(NameError, 'Each address number should not be null', convert_ipv4, '172..5.1')

    def test_exception_wrong_char_1(self):
        self.assertRaisesRegexp(NameError, 'Each number should in \[0-9\]', convert_ipv4, 'a172.168.5.1')

    def test_exception_wrong_char_2(self):
        self.assertRaisesRegexp(NameError, 'Each number should in \[0-9\]', convert_ipv4, '-172.168.5.1')

    def test_exception_wrong_char_3(self):
        self.assertRaisesRegexp(NameError, 'Each number should in \[0-9\]', convert_ipv4, '-0.168.5.1')

    def test_exception_wrong_char_4(self):
        self.assertRaisesRegexp(NameError, 'Each address number should be 3-digits', convert_ipv4, '0000.168.5.1')

    def test_exception_wrong_char_5(self):
        self.assertRaisesRegexp(NameError, 'Each address number should in \[0,255\]', convert_ipv4, '256.168.5.1')

    def test_exception_ne_4_numbers_1(self):
        self.assertRaisesRegexp(NameError, 'Invalid format of string, please make sure 4 address numbers are given',
                                convert_ipv4, '192.168.5.1.1')

    def test_exception_ne_4_numbers_2(self):
        self.assertRaisesRegexp(NameError, 'Invalid format of string, please make sure 4 address numbers are given',
                                convert_ipv4, '192.168.5')

if __name__ == '__main__':
    unittest.main()
