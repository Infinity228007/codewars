import math

import numpy as np


def get_matrix(key, message):
    new_message = message.replace(" ", "")
    every_third_char = [char for i, char in enumerate(new_message, start=1) if i % 3 == 0]
    other_chars = [char for i, char in enumerate(new_message, start=1) if i % 3 != 0]

    if len(other_chars) % 2 != 0:
        last_char = other_chars.pop()
    else:
        last_char = ""

    digraphs = [other_chars[i] + other_chars[i + 1] for i in range(0, len(other_chars), 2)]

    if last_char:
        digraphs.append(last_char)

    if len(other_chars) % 2 != 0:
        digraphs[-1] += " "

    result = [(a, b) for a, b in zip(digraphs, every_third_char)] + \
             [(a, None) for a in digraphs[len(every_third_char):]] + \
             [(None, b) for b in every_third_char[len(digraphs):]]

    flat_list = [item for pair in result for item in pair if item is not None]

    num_columns = len(str(key))
    num_rows = math.ceil(len(flat_list) / num_columns)

    num_spaces_to_add = num_columns - (len(flat_list) % num_columns)
    flat_list += [" "] * num_spaces_to_add

    return np.array(flat_list[:num_rows * num_columns]).reshape(num_rows, num_columns)


def get_order(key):
    key_str = str(key)
    order = sorted(range(1, len(key_str) + 1), key=lambda x: key_str[x - 1])
    return order


def print_columns_in_order(matrix, order):
    combined_string = "".join("".join(matrix[:, col - 1]) for col in order)
    combined_string = combined_string.replace(" ", "")
    return combined_string


def print_result(key, message):
    matrix = get_matrix(key, message)
    order = get_order(key)
    combined_string = print_columns_in_order(matrix, order)
    print(combined_string)
    return combined_string


key = 165432
message = "WORK SMART NOT HARD"
result = print_result(key, message)
assert result == 'WONOTARDMRKSHART', \
    f'{key} not OK, {result} != WONOTARDMRKSHART'

key = 231
message = "LLOHE"
result = print_result(key, message)
assert result == 'HELLO', \
    f'{key} not OK, {result} != HELLO'

key = 41325
message = "INCOMPLETECOLUMNARWITHALTERNATINGSINGLELETTERSANDDIGRAPHS"
result = print_result(key, message)
assert result == 'CECRTEGLENPHPLUTNANTEIOMOWIRSITDDSINTNALINESAALEMHATGLRGR', \
    f'{key} not OK, {result} != CECRTEGLENPHPLUTNANTEIOMOWIRSITDDSINTNALINESAALEMHATGLRGR'

key = 12
message = "HELLOWORLD"
result = print_result(key, message)
assert result == 'HELOORDLWL', \
    f'{key} not OK, {result} != HELOORDLWL'

key = 3412
message = "THISISJUSTATEST"
result = print_result(key, message)
assert result == 'SITASTTHJUESIST', \
    f'{key} not OK, {result} != SITASTTHJUESIST'

def to_camel_case(text):
    new_text = []
    text = text.split('-')
    for i in text:
        s = i.split('_')
        if len(s) == 1:
            new_text.append(s[0])
        else:
            for n in s:
                new_text.append(n)
    if not new_text[0].istitle():
        for i, n in enumerate(new_text[1:]):
            new_text[i + 1] = n.capitalize()
    return ''.join(new_text)


def count_bits(n):
    multiple_of_two = tuple(2 ** i for i in range(0, 100))
    new_n = ''
    multiple_new = ()
    if n == 0:
        return 0
    else:
        for k, i in enumerate(multiple_of_two):
            if i > n:
                multiple_new = multiple_of_two[0:k]
                break
        for i in multiple_new[::-1]:
            if n >= i:
                n -= i
                new_n += '1'
            else:
                new_n += '0'
    return new_n.count('1')


print(count_bits(3211))


def disemvowel(string_):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in string_ if char not in vowels)


print(disemvowel("This website is for losers LOL!"))


def pig_it(text):
    new_text = ''
    for word in text.split():
        for n, i in enumerate(word):
            if len(word) == 1 and word not in ('!', '#'):
                new_text += (i + 'ay ')
            elif word in ('!', '#'):
                new_text += i + ' '
            else:
                if n + 1 == len(word):
                    new_text += (i + word[0] + 'ay ')
                elif n == 0:
                    new_text = new_text
                else:
                    new_text += i
    return new_text[:-1]


print(pig_it('O tempora o mores !'))
