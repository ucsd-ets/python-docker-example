import unittest
from pyapp import digit_search

class DigitSearch(unittest.TestCase):
    def setUp(self):
        self.retrieve_digits_as_strings = digit_search.retrieve_digits_as_strings
        self.strings_list_to_digits_list = digit_search.strings_list_to_digits_list
    def test_digit_search(self):
        sentences = [
            "There are 360 degrees in a circle.",
            "Pi is approximately 3.14."
        ]
        for sentence in sentences:
            #First assertion test checks if self.retrieve_digits_as_strings returns a list
            self.assertTrue(isinstance(digits_as_strings := self.retrieve_digits_as_strings(sentence), list))
            #Second assertion test checks if every element of digits is a string
            self.assertTrue(all(list(map(lambda digit: isinstance(digit, str), digits_as_strings))))
            #Third assertion test checks if self.strings_list_to_digits_list returns a list
            self.assertTrue(isinstance(digits_as_integers := self.strings_list_to_digits_list(digits_as_strings), list))
            #Fourth assertion test checks if every element of digits is an int
            self.assertTrue(all(list(map(lambda digit: isinstance(digit, int), digits_as_integers))))
            #Print output for user
            print(f'Sentence: "{sentence}"')
            print(f'List of digits as strings: {digits_as_strings}')
            print(f'List of digits as integers: {digits_as_integers}')
            print('\n')

        
