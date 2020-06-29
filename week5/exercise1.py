# -*- coding: UTF-8 -*-
"""Refactoring.

This exercise contains a complete and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    print("Getting ready to start in 9")
    print("Getting ready to start in 8")
    print("Getting ready to start in 7")
    print("Getting ready to start in 6")
    print("Getting ready to start in 5")
    print("Getting ready to start in 4")
    print("Getting ready to start in 3")
    print("Getting ready to start in 2")
    print("Getting ready to start in 1")
    print("Let's go!")

    triangle = {"base": 3, "height": 4}
    triangle["hypotenuse"] = triangle["base"] ** 2 + triangle["height"] ** 2
    print("area = " + str((triangle["base"] * triangle["height"]) / 2))
    print("side lengths are:")
    print("base: {}".format(triangle["base"]))
    print("height: {}".format(triangle["height"]))
    print("hypotenuse: {}".format(triangle["hypotenuse"]))

    another_hyp = 5 ** 2 + 6 ** 2
    print(another_hyp)

    yet_another_hyp = 40 ** 2 + 30 ** 2
    print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):

    while start >= stop:
        print(message + " " + str(start))
        start -= 1
    print(completion_message)





# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    hypotenuse = (base**2 + height**2)**(1/2)
    return hypotenuse
    

def calculate_area(base, height):
    return base * height / 2


def calculate_perimeter(base, height):
    return calculate_hypotenuse(base, height) + base + height


def calculate_aspect(base, height):
    if base > height:
        return "wide"
    elif base == height:
        return "equal"
    else:
        return "tall"


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    return {
        "area": calculate_area(base, height),
        "perimeter": calculate_perimeter(base, height),
        "height": height,
        "base": base,
        "hypotenuse": calculate_hypotenuse(base, height),
        "aspect": calculate_aspect(base, height),
        "units": units,
    }


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}""".format( height=facts_dictionary["height"], 
            hypotenuse=facts_dictionary["hypotenuse"],
            base=facts_dictionary["base"])
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}""".format( height=facts_dictionary["height"], 
            hypotenuse=facts_dictionary["hypotenuse"],
            base=facts_dictionary["base"])
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}""".format( height=facts_dictionary["height"], 
            hypotenuse=facts_dictionary["hypotenuse"],
            base=facts_dictionary["base"])

    pattern = (
        "This triangle is {area}{units}²\n"
        "It has a perimeter of {perimeter}{units}\n"
        "This is a {aspect} triangle.\n"
    ).format(area=facts_dictionary["area"], 
            units=facts_dictionary["units"],
            aspect=facts_dictionary["aspect"],
            perimeter=facts_dictionary["perimeter"])
    if facts_dictionary["aspect"] == "tall":
        return tall + pattern
    elif facts_dictionary["aspect"] == "equal":
        return equal + pattern
    else:
        return wide+pattern
    # return tall


def triangle_master(base, height, return_diagram=False, return_dictionary=False):
    if return_diagram==False and return_dictionary==False:
        return None
    elif return_dictionary==False:
        return "diagram" 
    elif return_diagram==False:
        return {"diagram":True, "return_dictionary":True, "units":"units"}
    else:
        return {"diagram":"diagram", "return_dictionary":True}
    # elif return_diagram==True:
    #     return None
    # elif return_dictionary:
    #     return None
    # else:
    #     print("You're an odd one, you don't want anything!")


def randomString(stringLength):
    import string
    import random
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def String(stringLength):
    import string
    import random
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

            
def get_a_word_of_length_n(length):
    if length == 0:
        return None
    try:
        int(length)
        return randomString(int(length))
    except Exception:
        return None


def list_of_words_with_lengths(list_of_lengths):
    word = []
    for length in list_of_lengths:
        word.append(randomString(length))
    return word


def wordy_pyramid():
    buff = []
    start = 3
    end = 20
    temp = start
    flag = 0
    while start <= end + 1:
        if start == end + 1:
            flag = 1
        if flag == 0: 
            buff.append(start)
            start = start + 2
        else: 
            buff.append(end) 
            start = temp + 1
            end = end - 2
    return list_of_words_with_lengths(buff)


if __name__ == "__main__":
    do_bunch_of_bad_things()
    wordy_pyramid("a2a73e7b926c924fad7001ca3111acd55af2ffabf50eb4ae5")
