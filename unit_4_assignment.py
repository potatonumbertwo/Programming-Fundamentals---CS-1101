def is_power(a, b):
    """ define a function that a is a power of b if a is divisible by b
    and a/b is a power of b ,returns True if a is a power of b"""
    isADivisibleByB = is_divisible(a, b) == 1
    isADiviedByBIsPowerofB = (a / b) % b == 0
    if isADivisibleByB and isADiviedByBIsPowerofB:
        return True
    # if a == b:
    #     return True
    # if b == 1:
    #     return False
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


# def is_power(a, b):
#     if a == b:
#         return True
#     if b == 1:
#         return False
#     elif a % b != 0:
#         return False
#     else:
#         return is_power(a / b, b)


# print("is_power(10, 2) returns: ", is_power(10, 2))
# print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
# print("is_power(10, 1) returns: ", is_power(10, 1))
# print("is_power(3, 3) returns: ", is_power(3, 3))
# print(is_power(64, 2))
