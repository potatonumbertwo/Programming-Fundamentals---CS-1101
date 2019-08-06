# def right_justify(s):
#     len_70 = print(len(' ')
#     len(s))

# d = {1: 3, 2: 3, 4: 2}
# v = [2, 3, 5]
# for k in d:
#     if d[k] == v:
# return k
#
# print(dict().get("no", "help!"))
#
#
# print((0, 1, 5, 2) > (0, 1.0, 4, 3.1))

alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def has_duplicates(string_to_analysis):
    """ define a function called has_duplicates that takes a string parameter and
       returns True if the string has any repeated characters. Otherwise,return False"""
    for sting in test_dups:
        return True


def test_and_print(strings_list):
    for string in strings_list:

        output = has_duplicates(string)
        if output is True:
            print(string + ' has duplicates')
        else:
            print(string + ' has no duplicates')


test_and_print(test_dups)

# if h == 1:
#     output_duplicates = str.format('{} has duplicates', test_dups[i])
#     print(output_duplicates)
# else:
#     output_without_duplicates = str.format('{} has no duplicates', )
#     print(output_without_duplicates)


# print(has_duplicates())
