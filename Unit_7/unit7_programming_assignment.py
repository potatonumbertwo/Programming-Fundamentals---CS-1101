# class Unit7:
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     test_dups = ["zzz", "dog", "bookkeeper", "subdermatoglyphic", "subdermatoglyphics"]
#     test_miss = ["zzz", "subdermatoglyphic", "the quick brown fox jumps over the lazy dog"]
#
#     # From Section 11.2 of: 
#     # Downey, A. (2015). Think Python: How to think like a computer scientist.
#     # Needham, Massachusetts: Green Tree Press. 
#
#     def histogram(self, s):
#         d = dict()
#         for c in s:
#             if c not in d:
#                 d[c] = 1
#             else:
#                 d[c] += 1
#         return d
#
#     # print(histogram())
#
#     def has_duplicates(self, string_to_analyze):
#         """ define a function called has_duplicates that takes a string parameter and
#         returns True if the string has any repeated characters. Otherwise,return False"""
#         for i in enumerate(string_to_analyze):
#             histogram
#                 return True
#
#
#     # print(has_duplicates())
#
#     def missing_letters(new_string):
#         """ define a function called missing_letters that takes a string parameter
#         and returns a new string with fileNamesList the letters of the alphabet
#         that are not in the argument string.
#         The letters in the returned string should be in alphabetical order."""
#         filter_letter = []
#         for i in new_string:
#             if i not in new_string:
#                 filter_letter.append()


# # Create a tuple containing 4 strings
# numbers_tuple = ("zero", "one", "two", "three")
#
# # Create a list containing 4 numbers
# numbers_list = [0, 1, 2, 3]
#
# # Create a zip object of that combines the tuple and the corresponding element from the list.
# numbers_zip = zip(numbers_list, numbers_tuple)
#
# # Every element in the zip object is a tuple
# for o in numbers_zip:
#     print(o)
#
# numbers_tuple = ("zero", "one", "two", "three")
# numbers_enumerate = enumerate(numbers_tuple)
# for number in numbers_enumerate:
#     print(number)


