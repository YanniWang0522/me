# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time




def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # try to find 3
    # for i in array:
    #   if i == 3:
    #      found it 
 
    # 5,  5 > 3, 5 - 10 not considered 1
    # 3,                               2 


    # 0..100  50  1
    # 50..100 75  2 
    # 50..75  62  3
    # 62..75  68  4
    # 68..75  71  5
    # 71..75  73  6
    # 73..75  74  7

    # guess = (high + low) // 2

    # treies = 1


    # if guess > actual_number: 
    #     high = guess
    # else:
    #     low  = guess


    tries = 0
    while True:

        if (high - low) == 2:
            break

        guess = (high + low) // 2
        tries = tries + 1

        if actual_number == guess:
            break
        elif guess > actual_number: 
            high = guess
        else:
            low  = guess


    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(0, 100, 74))
    # print(binary_search(1, 100, 95))
    # print(binary_search(1, 51, 5))
    # print(binary_search(1, 50, 5))
