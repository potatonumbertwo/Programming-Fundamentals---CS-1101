def is_power(a, b):
    """ define a function that a is a power of b if a is divisible by b
    and a/b is a power of b ,returns True if a is a power of b"""

    if a == b:
        return True
    if b == 1:
        return False
    isADivisibleByB = is_divisible(a, b) == 1
    isADiviedByBIsPowerofB = a / b % b == 0
    if isADivisibleByB and isADiviedByBIsPowerofB:
        return is_power(a / b, b)
    #
    else:
        return False


# print(is_divisible(10, 2))
# print(is_divisible(27, 3))
# print(is_divisible(1, 1))
# print(is_divisible(10, 1))
# print(is_divisible(3, 3))


def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))

