# numbers = [1, 2, 3, 4, 5, 6]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
#     print(numbers[i])
#

# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#
#     return res
#
#
# print(capitalize_all('potato'))


# sentence = 'The purpose of human life is to serve , and to show compassion and the will to help others .'
# words = sentence.split()
# print(words)


'''
values are characters ,numbers,lists,boolean
Object is a assigned variable with values
Equivalent is that two list have the same elements
Identical is that two list have the some object
# '''
#
# vegetables = ['sweet potato', 'carrot', 'tomato']
# # fruits = ['sweet potato', 'carrot', 'tomato']
# fruits = vegetables
# print(vegetables is fruits)
#
# '''
# objects, references, and aliasing
#
# object: Something a variable can refer to. An object has a type and a value.
#
# reference is the association between a variable and its value.
#
# aliasing: A circumstance where two or more variables refer to the same object.
#
# If a refers to an object and you assign b = a, then both variables refer to the same object:
#
# '''
# vegetables = ['sweet potato', 'carrot', 'tomato']  # this is an object
# fruits = ['sweet potato', 'carrot', 'tomato']  # vegetables and fuits are aliased
# fruits = vegetables  # This  ia reference example
# potato = vegetables[0]
# print(potato)
# print(vegetables is fruits)

'''


'''

#
# def split_word(t):
#     delimiter = '_'
#     return t.split(delimiter)
#
#
# split_list = split_word('upper_case')
#
# print(split_list)

#
# def word_joint(t):  # t is the parameter
#     delimiter = ' '
#     return delimiter.join(t)
#
#
# def remove_comma(a):
#     return a.remove(',')
#
#
# words = ['The', 'purpose', 'of', 'human', 'life', 'is', 'to', 'serve', ',', 'and', 'to', 'show', 'compassion', 'and',
#          'the', 'will', 'to', 'help', 'others', '.']  # this is an object
#
# sentence = word_joint(words)  # words is an argument and it reference t in the function
# sentence_index = words.count(words)

# sentence = remove_comma(sentence)
# print(sentence_index)

#
# def remove_zero(a):
#     del a[-1]
#
#
# numbers = [2, 3, 4, 5, 2, 0, 4, 0, 3, 0, 2, 1, 0, 6, 8, 9, 0, 90]
# remove_zero(numbers)
# print(numbers)


# def remove_zero(a):
#     for i in a:
#         if i == 0:
#             a.remove(0)
#
#
# numbers = [2, 3, 4, 5, 2, 0, 4, 0, 3, 0, 2, 1, 0, 6, 8, 9, 0, 90]
# remove_zero(numbers)
# print(numbers)

#


# SELFQUIZ
# mylist = [[2, 4, 1], [1, 2, 3], [2, 3, 5]]
# a = 0
# total = 0
# while a < 3:
#     b = 0
#     while b < 2:
#         total += mylist[a][b]
#         b += 1
#     a += 1
# print(total)

# index = "Ability is a poor man's wealth".find("W")
# print(index)
# index = "Ability is a poor man's wealth".find("w")
# print(index)


#
# mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
# print(" ".join(mylist[1::2]))
#
#
# print('Unit 6'[-1] )
#
# fruit = "banana"
# letter = fruit[1]
# print (letter)
#
# #
# for fruit in ["banana", "apple", "quince"]:
#     print (fruit)


# my_list = [3, 2, 1]
# print(my_list.sort())
#
# mylist = ["now", "four", "is", "score", "the", "and seven", "time", "years", "for"]
# a = 0
# while a < 8:
#     print(mylist[a], )
#     a = a + 2
#
# mylist = [[2, 4, 1], [1, 2, 3], [2, 3, 5]]
# total = 0
# for sublist in mylist:
#     total += sum(sublist)
# print(total)
#
# index = "Ability is a poor man's wealth".find("w")
# print(index)
#


# mylist = [ [2,4,1], [1,2,3], [2,3,5] ]
# a=0
# total = 0
# while a < 3:
#     b = 0
#     while b < 2:
#         total += mylist[a][b]
#         b += 1
#     a += 1
# print(total)


# milk = ['white']
# chalk = ['white']
#
# print(milk is chalk)


# s = "help"
# for letter in s[1:]:
#       last = letter
#       break
# print(last)
#
#
# pi = int(3.14159)
# print (pi)


# n = 10
# while n != 1:
#     print(n,)
#     if n % 2 == 0: # n is even
#         n = n / 2
#     else: # n is odd
#         n = n * 3 + 1


# s = "Python3"
# print(s[len(s)])


# x=1
# y=2
# if x == y:
#     print (x, "and", y, "are equal")
# else:
#     if x < y:
#         print (x, "is less than", y)
#     else:
#         print (x, "is greater than", y)
# def is_divisible(x, y):
#     return (x % y) == 0
#
#
# print(is_divisible(4, 2))
#
# pi = float(3.14159)
# print(pi)
#
#
# def area(tokens, w):
#     temp = tokens * w
#     return temp
#
#
# tokens = 4.0
# w = 3.25
# x = area(tokens, w)
# if (x):
#     print(x)

# word = 'bAnana'
#
# index = word.find('a')
# print(index)

#
# def print_n(s, n):
#     if n > 0:
#         print(s)
#         print_n(s, n - 1)
#     return n
#
#
# n = 3
# while print_n("hi", n):
#     print_n("there!", n)
#     n = 0


s = "help"
for letter in s[1:]:
    last = letter
    break
print(last)

print('Unit 6'[-1])

n = 2
n += 5
print(n)
