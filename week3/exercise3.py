"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(number):
    while True:
        try:
          number = int(number) 
          return number 
        except Exception:
          number = input("it is not a number, plz enter again ")

def check_upper(upper, lower):

    upper = not_number_rejector(upper)

    while upper <= lower:
      
      upper = input("the upper bound should be lager than lower, plz enter again : ")
      upper = not_number_rejector(upper)

    return upper

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """


    print("\nWelcome to the guessing game!")
    lowerBound = input("Enter the lower bound: ")
    lowerBound = not_number_rejector(lowerBound)

    upperBound = input("Enter the upper bound: ")
    upperBound = check_upper(upperBound, lowerBound)
    
  
    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    
    while not guessed:
        guessedNumber = (input("Guess a number: "))
        guessedNumber = not_number_rejector(guessedNumber)
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif  guessedNumber < lowerBound or guessedNumber > upperBound:
            print("Wrong! Out of range set before, try again OvO")
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"

    # print(actualNumber)
    
    
    # return





if __name__ == "__main__":
    print(advancedGuessingGame())
