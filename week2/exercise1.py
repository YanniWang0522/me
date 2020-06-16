"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# create an array, contains the strings 'what', 'does', 'this', 'line', 'do', '?'
some_words = ['what', 'does', 'this', 'line', 'do', '?']

# it will print the elements in the array each line
for word in some_words:
    print(word)

# it will print the elements in the array each line, the variable name is X is not a word
for x in some_words:
    print(x)

# it will print all array in the single line
print(some_words)

# length = size of array = number of strings, if it is bigger than 3, then the word
if len(some_words) > 3:
    print('some_words contains more than 3 words')

# Define a function
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
# print your local machines environment and details of local machine
    print(platform.uname())

# Call the function defined before, with no paramater
usefulFunction()
