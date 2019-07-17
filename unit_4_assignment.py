def is_power(a, b):
    """ define a function that a is a power of b if a is divisible by b
    and a/b is a power of b ,returns True if a is a power of b"""

    if a == b:  # base case of two arguments are equal
        return True
    if b == 1:
        return False  # base case of the second argument is 1
    isADivisibleByB = is_divisible(a, b) == 1  # assign is_divisible() to a variable to check is_divisible is True
    isADiviedByBIsPowerofB = a / b % b == 0  # variable checks a/b is power of b ,== mean equal here
    if isADivisibleByB and isADiviedByBIsPowerofB:
        return is_power(a / b, b)  # call itself recursively

    else:
        return False


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
