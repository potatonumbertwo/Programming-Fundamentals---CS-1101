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
    histogram_dict = histogram(string_to_analysis)
    for frequency in histogram_dict.values():
        if frequency > 1:
            return True

    return False


for string in test_dups:
    output = has_duplicates(string)
    if output is True:
        print(string + ' has duplicates')
    else:
        print(string + ' has no duplicates')


def missing_letters(string):
    """ define a function called missing_letters that takes a string parameter
    and returns a new string with all the letters of the alphabet
    that are not in the argument string.
    The letters in the returned string should be in alphabetical order."""
    missing_letters_string = str()
    histogram_dict = histogram(string)
    for letter in alphabet:
        frequency_of_letter = histogram_dict.get(letter)
        if frequency_of_letter is None:
            missing_letters_string += letter
    return missing_letters_string


for word in test_miss:
    missed_letters_in_word = missing_letters(word)
    print(test_miss[word])
    print(missed_letters_in_word)
