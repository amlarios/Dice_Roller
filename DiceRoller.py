#Alessio Larios
#Dice Roller
#March 11, 2017

import random
from collections import Counter

def main():

    questions()

    return

class dice(object):

    def __init__(self,sides=0):

        self.sides = sides

    def roll(self,sides):

        '''Chooses a random number from the given number of sides.'''

        result = random.randint(1,sides)
        return result

def questions():

    '''Allows user to determine which functions of program to utilize.'''

    valid = True
    while valid == True:
        number_of_dice_in = str(raw_input('How many dice would you like? ')).lower().strip()
        try:
            if text2int(number_of_dice_in) > 0:
                number_of_dice = text2int(number_of_dice_in)
                valid = False
            elif text2int(number_of_dice_in) <= 0:
                print('That is not a valid response.')
        except Exception:
            try:
                if int(number_of_dice_in) > 0:
                    number_of_dice = int(number_of_dice_in)
                    valid = False
                else:
                    print('That is not a valid response.')
            except ValueError:
                print ('That is not a valid response.')
    valid = True
    while valid == True:
        number_of_sides_in = str(raw_input('How many sides would you like the dice to have? ')).lower().strip()
        try:
            if text2int(number_of_sides_in) > 0:
                number_of_sides = text2int(number_of_sides_in)
                valid = False
            elif text2int(number_of_sides_in) <= 0:
                print('That is not a valid response.')
        except Exception:
            try:
                if int(number_of_sides_in) > 0:
                    number_of_sides = int(number_of_sides_in)
                    valid = False
                else:
                    print('That is not a valid response.')
            except ValueError:
                print ('That is not a valid response.')
    result_of_dice = dice_and_sides(number_of_dice,number_of_sides)
    if len(result_of_dice) == 1:
        ask_redo()
    else:
        valid = True
        while valid == True:
            avg_in = str(raw_input('Would you like the average of the dice? ')).lower().strip()
            if avg_in.startswith('y'):
                print find_average(result_of_dice)
                valid = False
            elif avg_in.startswith('n'):
                valid = False
            else:
                print('That is not a valid response.')
        valid = True
        while valid == True:
            med_in = str(raw_input('Would you like the median of the dice? ')).lower().strip()
            if med_in.startswith('y'):
                print find_median(result_of_dice)
                valid = False
            elif med_in.startswith('n'):
                valid = False
            else:
                print('That is not a valid response.')
        valid = True
        while valid == True:
            mode_in = str(raw_input('Would you like the mode of the dice? ')).lower().strip()
            if mode_in.startswith('y'):
                print find_mode(result_of_dice)
                valid = False
            elif mode_in.startswith('n'):
                valid = False
            else:
                print('That is not a valid response.')
        valid = True
        while valid == True:
            mx_in = str(raw_input('Would you like the max of the dice? ')).lower().strip()
            if mx_in.startswith('y'):
                print find_max(result_of_dice)
                valid = False
            elif mx_in.startswith('n'):
                valid = False
            else:
                print('That is not a valid response.')
        valid = True
        while valid == True:
            mn_in = str(raw_input('Would you like the min of the dice? ')).lower().strip()
            if mn_in.startswith('y'):
                print find_min(result_of_dice)
                valid = False
            elif mn_in.startswith('n'):
                valid = False
            else:
                print('That is not a valid response.')
        ask_redo()

def dice_and_sides(number_of_dice,number_of_sides):

    '''Allows user to determine number of sides the dice should have. This is
       set up in such a way that users can use integers or spell numbers out.
       If the user input is not a number or is a number less than 0, the user
       is asked to give a different input.'''

    result_of_dice = []
    d = 0
    while d < number_of_dice:
        result_of_dice.extend([dice().roll(number_of_sides)])
        d = d+1
    print('The dice landed on '+str(result_of_dice)+'.')
    return result_of_dice

def find_average(result_of_dice):

    return (sum(result_of_dice)/len(result_of_dice))

def find_mode(result_of_dice):

    mode = Counter(result_of_dice).most_common(1)

    return mode[0][0]


def find_median(result_of_dice):

    n = len(result_of_dice)
    sorted_results = sorted(result_of_dice)

    if n == 1:
        med = sorted_results[0]
    elif n%2 == 0:
        n1 = n/2
        med = ((sorted_results[n1]+sorted_results[n1-1])/2)
    else:
        n1 = int(n/2)
        med = sorted_results[n1]

    return med

def find_min(result_of_dice):

    return min(result_of_dice)

def find_max(result_of_dice):

    return max(result_of_dice)


def ask_redo():

    '''Allows user to decide to roll again.'''

    redo = str(raw_input('Would you like to roll again? ')).lower().strip()
    if redo.startswith('y'):
        questions()
    elif redo.startswith('n'):
        return
    else:
        print('That is not a valid response.')
        ask_redo()

#This function was posted online by stackoverflow user recurisve. Here is the
#link:
#http://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
def text2int(textnum, numwords={}):

    '''Converts numbers that are written out into integer form.'''

    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
