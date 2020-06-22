TODO: Reflect on what you learned this week and what is still unclear.
 
 Revision: 
 Week2 Exercise0

def adder(a_number, another_number):

     the_answer = a_number + another_number

    return the_answer


def really_shout(a_string):
    """Return a string in uppercase, with an exclamation mark on the end.

    the_answer = shout(a_string) + "!"

    return the_answer


def shout_with_a_number(a_string, a_number):
    """Return a string in uppercase with a space and a_number concatentated.
   
    the_answer = a_string.upper() + " " + str(a_number)

    return the_answer

 Week2 Exercise3

def is_odd(a_number):
    """Return True if a_number is odd, and False if a_number is even.

    if a_number % 2 == 0:
        return False
    return True


def loops_1c(number_of_items=5, symbol="#"):

    Using any method, return a list of number_of_items items, each one a
    string with exacly one symbol in it.
    E.g.: ['#', '#', '#', '#', '#']

    symbol_array = []
    for i in range(number_of_items):
        symbol_array.append(symbol)
    return symbol_array


def loops_5():
    """Make the coordinates of the block.

    Return this:
    [
      ['(i0, j0)', '(i0, j1)', '(i0, j2)', '(i0, j3)', '(i0, j4)'],
      ['(i1, j0)', '(i1, j1)', '(i1, j2)', '(i1, j3)', '(i1, j4)'],
      ['(i2, j0)', '(i2, j1)', '(i2, j2)', '(i2, j3)', '(i2, j4)'],
      ['(i3, j0)', '(i3, j1)', '(i3, j2)', '(i3, j3)', '(i3, j4)'],
      ['(i4, j0)', '(i4, j1)', '(i4, j2)', '(i4, j3)', '(i4, j4)'],
      ['(i5, j0)', '(i5, j1)', '(i5, j2)', '(i5, j3)', '(i5, j4)'],
      ['(i6, j0)', '(i6, j1)', '(i6, j2)', '(i6, j3)', '(i6, j4)'],
      ['(i7, j0)', '(i7, j1)', '(i7, j2)', '(i7, j3)', '(i7, j4)'],
      ['(i8, j0)', '(i8, j1)', '(i8, j2)', '(i8, j3)', '(i8, j4)'],
      ['(i9, j0)', '(i9, j1)', '(i9, j2)', '(i9, j3)', '(i9, j4)']
    ]

    column = []
    for i in range(10): 
        row = []
        for j in range(5):
            row.append("(" + 'i' + str(i) + "," + " " + "j" + str(j) + ")")
        column.append(row) 
    return column


def loops_6():

    Return this:
    [
      ['0'],
      ['0', '1'],
      ['0', '1', '2'],
      ['0', '1', '2', '3'],
      ['0', '1', '2', '3', '4'],
      ['0', '1', '2', '3', '4', '5'],
      ['0', '1', '2', '3', '4', '5', '6'],
      ['0', '1', '2', '3', '4', '5', '6', '7'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
      ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ]

    column = []
    for i in range(10): 
        row = []
        j = 0

        while j <= i:
            row.append(str(j))
            j = j + 1
        column.append(row)
        
    return column

    space = " "
    star  = "*"

def loops_7():
    """Make a pyramid.

    Return this:
    [
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', '*', '*', '*', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    ]

    column = []
    for i in range(5): 
        star_start = 4 - i   
        star_end   = 4 + i 
        row = []

        for j in range(9):
            if j >= star_start and j <= star_end:
                row.append(star)
            else:
                row.append(space)

        column.append(row)

    return column
