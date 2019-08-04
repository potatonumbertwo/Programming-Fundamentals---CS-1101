alphabet = "abcdefghijklmnopqrstuvwxyz"
test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]


# From Section 11.2 of: 
# Downey, A. (2015). Think Python: How to think like a computer scientist.
# Needham, Massachusetts: Green Tree Press. 


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


def has_duplicates(strings):
    histogram(strings) > 1


print(has_duplicates('potato'))


def missing_letters(new_string):
    filter_letter = []
    for i in new_string:
        if i not in new_string:
            filter_letter.append()
