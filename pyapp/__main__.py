from .digit_search import retrieve_digits_as_strings, strings_list_to_digits_list
from .rotate_clockwise import rotate_clockwise

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


matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print("Check original matrix: ")
for row in matrix:
    print(*row)
rotate_clockwise(matrix)
print("Check matrix after rotated 90 degrees clockwise: ")
for row in matrix:
    print(*row)
