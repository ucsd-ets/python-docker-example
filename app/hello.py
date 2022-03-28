import app.digit_search as digit_search

def hello_world():
        return 'hello world!'

if __name__ == "__main__":
        sentences = [
            "There are 360 degrees in a circle.",
            "Pi is approximately 3.14."
        ]
        for sentence in sentences:
                print(f'Sentence: "{sentence}"')
                print(f'List of digits as strings: {(digits_as_strings := digit_search.retrieve_digits_as_strings(sentence))}')
                print(f'List of digits as integers: {(digits_as_integers := digit_search.strings_list_to_digits_list(digits_as_strings))}')
                print('\n')
