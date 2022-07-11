# def any_lowercase1(s):
#     for c in s:
#         if c.islower():
#             return True
#         else:
#             return False
#
#
# print(any_lowercase1('Potato'))
# print(any_lowercase1('poTato'))
# '''
#  The function check if c is lowercase ,if c is lowercase it returns True.
# if c is not lowercase it returns False.
# print(any_lowercase1('Potato')),The output return False.
# Because the function body is using for loop,if the first letter
# isn't lowercase it will return False ,and then end the loop.
#
# print(any_lowercase1('poTato')) output is True
#
# print(any_lowercase1('poTato')) returns True because the first letter is lowercase,
# it will keep checking,it will stop until it isn't lowercase.
# '''
#
#
# def any_lowercase2(s):
#     for c in s:
#         if 'c'.islower():
#             print('c')
#             return 'True'
#         else:
#             return 'False'
#
#
# print(any_lowercase2('Potato'))
#
# '''
# This function is check if 'c' is lowercase.And it will always turns string True.
# Because it won't check the c in s,it only checks 'c'
# if we change the function like this,
# '''
#
#
# def any_lowercase2(s):
#     for c in s:
#         if 'C'.islower():
#             print('c')
#             return 'True'
#         else:
#             return 'False'
#
#
# print(any_lowercase2('Potato'))
#
# '''
# it will turn string False ,because 'C' is uppercase.
#
# '''


def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


print(any_lowercase3('PotatO'))

# '''
# This function checks any lowercase in s,if it is not lowercase it will keep running
# until all letter from s to be checked. it returns True if it has at least one lowercase.
# This example returns True because there are 5 lowercase letters.
# '''
#
#
# def any_lowercase4(s):
#     flag = False
#     for c in s:
#         flag = flag or c.islower()
#     return flag


# print(any_lowercase4('Potato'))
# print(any_lowercase4('POTATO'))
#
# '''
# any_lowercase4 function is check if c in s has any lowercase.If c is lowercase,
# then return False or True ,and keep running until all letter from c to be checked.
# If there is any lowercase it will return True.
# print(any_lowercase4('POTATO')) will return False because there hasn't any lowercase.
#
# '''
#
#
# def any_lowercase5(s):
#     for c in s:
#         if not c.islower():
#             return False
#
#     return True
#
#
# print(any_lowercase5('Potato'))
# print(any_lowercase5('potato'))
#
# '''
# any_loercase5 function checks the c.islower is True or False. It's check all letter in s hast to be lowercase .
# If there is any uppercase it will return False
#
# print(any_lowercase5('Potato')) return False, Because the first letter 'P' is not lowercase so return False
# directly and then end this program.
#
# However , print(any_lowercase5('potato')) will return True which means if it's lowercase,will keep running
# until find any not lowercase and then end the program
# '''
