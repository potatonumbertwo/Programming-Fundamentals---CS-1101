def division(a, b):
    try:
        y = a / b
        return y
    except ZeroDivisionError:
        print('b should not be 0')


print(division(9, 3))
print(division(3, 0))
"""
Output:
3.0
b should not be 0
To fix the ZeroDivisionError, we could assign b =! 0 before return value
"""


def x_times_y():
    try:
        x = input('input a number')
        y = input('input another number')
        z = x * y
        return z
    except TypeError:
        print('TypeError,y should convert into int or float')


print(x_times_y())

"""
Output:
input a number 4
input another number 4
TypeError,y should convert into int or float
should assign x and x value first
To fix this TypeError we can use type() to check the input value first
"""


def name_error():
    try:
        y = x / z
        print(y)
    except NameError:
        print('should assign x and x value first')


name_error()

'''
Output
should assign x and x value first
To fix the NameError we should assign x and z value either local or global
'''