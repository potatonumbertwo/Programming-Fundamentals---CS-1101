def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False


def is_power(a, b):
    if a == b == 1:
        return 1
    elif b == 1:
        return a
    elif a and b > 0:
        return is_divisible(a, b)


print("is_power(10, 2) returns: ", is_power(10, 2))
print("is_power(27, 3) returns: ", is_power(27, 3))
print("is_power(1, 1) returns: ", is_power(1, 1))
print("is_power(10, 1) returns: ", is_power(10, 1))
print("is_power(3, 3) returns: ", is_power(3, 3))
