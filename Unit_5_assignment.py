import math


def my_sqrt(a):
    """ define a function named my_sqrt,take a as a parameter,
    using while loop to calculate square root,and returns the square root"""
    x = 10

    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        x = y


def test_sqrt():
    """define a function named test_sqrt, using my_sqrt function
    to compare with math.sqrt,print out their difference"""
    for i in range(1, 26):
        mysqrt = my_sqrt(i)

        math_sqrt = math.sqrt(i)

        diff = abs(math_sqrt - float(mysqrt))

        print('a = ' + str(i) + ' | ' + 'my_sqrt(' + str(i) + ') = ' + str(my_sqrt(i)) + ' | ' + 'math.sqrt(' + str(
            i) + ') = ' + str(math.sqrt(i)) + ' | ' 'diff = ' + str(diff))


test_sqrt()
