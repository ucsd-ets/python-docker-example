from .digit_search import retrieve_digits_as_strings, strings_list_to_digits_list

sentences = [
    "There are 360 degrees in a circle.",
    "Pi is approximately 3.14."
]
for sentence in sentences:
    print(f'Sentence: "{sentence}"')
    digits_as_strings = retrieve_digits_as_strings(sentence)
    print(f'List of digits as strings: {digits_as_strings}')
    digits_as_integers = strings_list_to_digits_list(digits_as_strings)
    print(f'List of digits as integers: {digits_as_integers}')
