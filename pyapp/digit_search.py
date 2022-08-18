import re
from typing import List

def retrieve_digits_as_strings(sentence: str) -> List[str]:
    """
    Uses RegEx to find all digits in a string sentence.

    Args:
        sentence: A sentence that is stored in a string.
    
    Returns:
        A list of digits found in the sentence stored as strings.

    Raises:
        TypeError: If the sentence argument is an incorrect type
    """
    if not isinstance(sentence, str):
        raise TypeError("sentence argument must be of type <str>")
    return re.findall("\d", sentence)

def strings_list_to_digits_list(strings_list: List[str]) -> List[int]:
    """
    Converts a list of digits stored as strings to a list of integers.

    Args:
        strings_list: List of digits stored as strings
    
    Returns:
        digits_list: A list of digits as integers
    
    Raises:
        TypeError: If strings_list is not a list of digits stored as strings
        ValueError: If string in strings_list cannot be casted to an integer
    """

    digits_list = list()

    for index, digit in enumerate(strings_list):
        if not isinstance(digit, str):
            raise TypeError("strings_list argument must be of type <list[str]>")
        else:
            try:
                digits_list.append(int(digit))
            except:
                raise ValueError(f"{digit} at index {index} of strings_list is not a digit stored as a string. It cannot be converted to an integer.")
                
    return digits_list