import math


def my_sqrt(a):
    x = 10

    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        x = y


def test_sqrt():
    for i in range(1, 26):
        mysqrt = my_sqrt(i)

        math_sqrt = math.sqrt(i)

        diff = abs(math_sqrt - float(mysqrt))

        # print('a = ' + str(i) + ' | ' + 'my_sqrt(' + str(i) + ') = ' + str(my_sqrt(i)) + ' | ' + 'math.sqrt(' + str(
        #     i) + ') = ' + str(math.sqrt(i)) + ' | ' 'diff = ' + str(diff))

        # print('{}, {}, {},{}'.format(a=i, my_sqrt=mysqrt, math_sqrt=math_sqrt, diff=diff))


test_sqrt()
