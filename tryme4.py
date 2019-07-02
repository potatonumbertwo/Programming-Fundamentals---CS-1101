def new_line():  # define a function named new_line
    print('.')  # this function print out a '.'


def three_lines():  # define a function by using the new_line function

    # three_lines function will print out 3 lines this
    new_line()
    new_line()
    new_line()


def nine_lines():  # define a function named nine_lines
    # to get total of nine lines by using three_lines() function 3 times
    three_lines()
    three_lines()
    three_lines()


def clear_screen():  # add a function named clear_screen without parameter

    # function body combines nine_lines,three_lines,new_line to get total 25 lines

    nine_lines()  # call the nine_lines()function to print out 9 lines code
    print('This is 9th lines')
    nine_lines()
    three_lines()
    three_lines()
    new_line()
    print('Total 25 lines')


clear_screen()  # Call clear_screen will print out total 25 lines
