def new_line():  # define a function named new_line
    print('.')  # this function print out a '.'


def three_lines():  # define a function by using the new_line function

    new_line()
    new_line()
    new_line()


def nine_lines():  # define a function named nine_lines
    # to get total of nine lines by using three_lines() function 3 times
    three_lines()
    three_lines()
    three_lines()


# print('Call nine_lines()')


def clear_screen():  # add a function named clear_screen

    # function body combines nine_lines,three_lines,new_line
    # to get
    nine_lines()

    nine_lines()
    three_lines()
    three_lines()
    new_line()


# nine_lines()  # call the nine_lines()function to print out 9 lines code
# three_lines()  # call the three_lines function will print out 3 dot
clear_screen()

"""

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")


# print_lyrics()


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()

"""

'''
from math import pi  # import math module
# Math module provides mathematical function , if we want to use in our function we have to
# # import the math module.In this function I only import the mathematical constant pi from math module

def circle_perimeter(radius):  # define the function name circle_perimeter, radius as parameter
    # """ define a function for a circle perimeter """
    a = 2  # a= 2 is a local variable that only works within the function
    perimeter = a * pi * radius
    print(perimeter)


circle_perimeter(5)  # call function will return a value,pass 5 as the function argument.


output:
31.41592653589793

'''
#
# import math  # import math module
#
#
# def print_volume(r):  # define a function named print_volume,r is parameter of the function
#     volumes = 4 / 3 * math.pi * r ** 3
#     print(volumes)
#
#
# # call the function print_volume() pass a value as argument
# print_volume(5)
# print_volume(2)
# print_volume(7)



