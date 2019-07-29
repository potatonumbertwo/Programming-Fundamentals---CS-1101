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


print(my_sqrt(8))


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

# import math
#
#
# def mysqrt(a):
#     x = 1.1
#     while True:
#         y = (x + a / x) / 2.0
#         if y == x:
#             break
#         x = y
#     return x
#
#
# def test_square_root():
#     a = 1
#     while a < 26:
#         mine = mysqrt(a)
#         maths = math.sqrt(a)
#         diff = abs(mine - maths)
#         print("a =", a, "| mysqrt(a) =", mine, "| math.sqrt(a) = ", maths, " | diff = ", diff)
#         a = a + 1
#
#
# test_square_root()


import math


def my_sqrt(a):
    x = 1
    while True:
        y = (x + a / x) / 2.0
        if y == x:
            return y
        x = y


def test_sqrt():
    for i in range(1, 26):
        print("a =", i, "|", "my_sqrt(a) =", my_sqrt(i), "|", "math.sqrt(a) =",
              math.sqrt(i), "|", "diff =", abs(my_sqrt(i) - math.sqrt(i))
              )


test_sqrt()
