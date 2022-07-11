
# part 1

import math


# step 1 define a function writer the function header
def hypotenuse(length, width):
    return 0.0


print(hypotenuse(3, 4))  # output 0.0


# step 2 write the function body
def hypotenuse(length, width):
    length_squared = length ** 2
    width_squared = width ** 2
    return 0.0


print(hypotenuse(3, 4))  # output 0.0


# step 3 adding return value
def hypotenuse(length, width):
    length_squared = length ** 2
    width_squared = width ** 2
    hypotenuse_length = math.sqrt(length_squared + width_squared)
    return hypotenuse_length


# print out the statement
print(hypotenuse(3, 4))  # output:5.0


# step4 consolidate multiple statements into compound expressions.
def hypotenuse(length, width):
    return math.sqrt(length ** 2 + width ** 2)


print(hypotenuse(5, 7))
print(hypotenuse(8, 13))

'''
output：
8.602325267042627
15.264337522473747
'''




# part 2
# step 1 define a function called slope_intercept take 5 parameters.
def slope_intercept(x, x1, y1, x2, y2):
    '''define a function compute y value slope and intercept giving two points'''
    return 0


print(slope_intercept(6, 1, 2, 3, 4))  # it  print 0 because return is 0


# step 2  write function body find slop m.
def slope_intercept(x, x1, y1, x2, y2):
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
    return 0


print(slope_intercept(2, 3, 2, 5, 4))  # output is  0


# step 3  adding intercept b.
def slope_intercept(x, x1, y1, x2, y2):
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1

        return 0


# step 4 return value
print(slope_intercept(77, 3, 2, 5, 0))  # output is  0


# step 3  adding intercept b.
def slope_intercept(x, x1, y1, x2, y2):
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        y = x * m + b
        # a better idea to print out a y function using format but i don't know how to do that yet
        print(' y = ' + str(x) + " * " + str(m) + " + " + str(b))

        return y


print(slope_intercept(9, 3, 2, 5, 4))
print(slope_intercept(33, 5, 27, 90, 23))
print(slope_intercept(100, 8, 7, 25, 54))

'''
output
 y = 9 * 1.0 + -1.0
8.0
 y = 33 * -0.047058823529411764 + 27.235294117647058
25.682352941176468
 y = 100 * 2.764705882352941 + -15.117647058823529
261.35294117647055
'''

# part3
'''
I feel my peer have seen my hard work of discussion assignment they always give me compliments and appreciate my work also give fair rate. I am trying to make clean format, sample explanation and creative function of math I have learned.
I found that not fileNamesList of our peers participated in the discussion, according the past four weeks’ discussion assignment. If my peer post before Tuesday, I would have responded whoever post in the discussion forum by checking their code and reading their explanation. I rated them by checking if they used their own words, code and example. I will write my suggestions according their post and rewrite code if it need to be fixed.


'''