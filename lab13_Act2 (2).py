# By submitting this assignment, I agree to the following:
#    "Aggies do not lie, cheat, or steal, or tolerate those who do"
#    "I have not given or received any unauthorized aid on this assignment"

#    Name: Olsi Sadiku, Dylan Craven, kamal, ben
#    Section:509
#    Assignment:Lab13_Act2
#    Date: 23 November 2019

from random import randint as rdi
import sys

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# default values
points = 0
amount = 5
yahtCount = [0]
runner1 = True

# this acts as a temporary int variable to calculate the total score of any player
# *gets reset to 0 every time you run getTotal before calculating total*
gTotal = [0]

# default score sheets for the player(s)
# elements 0-5 inclusive are upper card scores
# elements 6-12 are lower card score in order
# element 13 is the amount of yahtzee rolls after scoring the first one, i.e 0 is one yahtzee, 1 means 2 yahtzee's
scoreList1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def displayinstruction():
    """Prints the instructions on how to play Yahtzee"""
    print("\nGame Instructions")
    print("The object of Yahtzee is to obtain the highest score from throwing 5 dice. Each turn you may roll the dice up to 3 times, "
          "\nkeeping the dice you like each roll The game consists of 13 rounds. "
          "\nIn each round, you roll the dice and then score the roll in one of 13 categories. You must score once in each category. "
          "\nThe score is determined by a different rule for each category. The game ends once all 13 categories have been scored.")

def displayscoring():
    """Prints the rules for scoring"""
    print("\nScoring Instructions:")
    print("for the category you chose, your dice roll must meet the requirements to receive points")
    print("for all the categories no the upper card, the points are totaled by adding up the dice with the respective values")
    print("For 3 of a Kind, you must have at least three of the same die faces. If so, you total all the die faces and score that total")
    print("For 4 of a Kind, you must have at least four of the same die faces. If so, you total all the die faces and score that total")
    print("For a Full house, you must have at least three of the same die faces, coupled with 2 different dice that also match; 25 points")
    print("For a small straight, you must have 4 consecutive die faces of increasing value; 30 points")
    print("For a large straight, you must have 5 consecutive die faces of increasing value; 40 points")
    print("For a Yahtzee, you must have 5 die of the same face; 50 pints *if you roll another yahtzee you can chose a bonus of 100 pints*")
    print("For a chance, you add up all the faces of each die")
    print("Upper Bonus, if your upper card has a total of 63 or more, then you gain an additional 35 points")


def dices(amount):
    """ This function creates the 5 dices thrown
    """
    dicerolls = []
    for i in range(amount):
        dicenum = rdi(1, 6)
        dicerolls.append(dicenum)
    return dicerolls


def most_frequent(List):
    '''takes in dices_taken_out, return the most common integer'''
    return max(set(List), key=List.count)


def ones(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 0th element of list"""
    points = 0
    for num in dices_taken_out:
        if num == 1:
            points+=1
    if scoreList[0] > 0:
        print("This box has already been scored in, choose a different box to score in")
        return 1
    elif points == 0:
        print("There are no ones to score, select a different number to score in")
        return 1
    else:
        scoreList[0] = points
        return 0


def twos(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 1st element of list"""
    points = 0
    for num in dices_taken_out:
        if num == 2:
            points += 2
    if scoreList[1] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no twos to score, select a different number to score in")
        return 1
    else:
        scoreList[1] = points
        return 0


def threes(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 2nd element of list"""
    points = 0
    for num in dices_taken_out:
        if num == 3:
            points += 3
    if scoreList[2] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no threes to score, select a different number to score in")
        return 1
    else:
        scoreList[2] = points
        return 0


def fours(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 3rd element of list"""
    points = 0
    for num in dices_taken_out:
        if num == 4:
            points += 4
    if scoreList[3] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no fours to score, select a different number to score in")
        return 1
    else:
        scoreList[3] = points
        return 0


def fives(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 4th element of list"""
    points = 0
    for num in dices_taken_out:
        if num == 5:
            points += 5
    if scoreList[4] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no fives to score, select a different number to score in")
        return 1
    else:
        scoreList[4] = points
        return 0


def six(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 5th element of list"""
    points = 0
    for num in dices_taken_out:
        if num == 6:
            points += 6
    if scoreList[5] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no sixes to score, select a different number to score in")
        return 1
    else:
        scoreList[5] = points
        return 0


def threeofakind(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 6th element of list"""
    cnt = 0
    a = most_frequent(dices_taken_out)
    for num in dices_taken_out:
        if num == a:
           cnt+=1
    if cnt >= 3:
        points = 0
        for number in dices_taken_out:
            points+=number
    if scoreList[6] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no three of a kinds to score, select a different number to score in")
        return 1
    else:
        scoreList[6] = points
        return 0


def fourofakind(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 7th element of list"""
    cnt = 0
    a= most_frequent(dices_taken_out)
    for num in dices_taken_out:
        if num == a:
            cnt += 1
    if cnt >= 4:
        points = 0
        for number in dices_taken_out:
            points += number
    if scoreList[7] > 0:
         print("This box has already been scored in, choose a different box to score in")
         return 1
    elif points == 0:
        print("There are no four of a kinds to score, select a different number to score in")
        return 1
    else:
        scoreList[7] = points
        return 0


def fullhouse(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 8th element of list"""
    if sorted(dices_taken_out.count(card) for card in set(dices_taken_out)) == [2, 3]:
        scoreList[8] = 25
        return 0
    else:
        return 1


def smallstraight(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 9th element of list"""
    smallS = False
    dices_taken_out.sort()
    if dices_taken_out[1] == dices_taken_out[0]+1 and dices_taken_out[2] == dices_taken_out[1]+1 and dices_taken_out[3] == dices_taken_out[2]+1:
        smallS = True
        points = 30
    if dices_taken_out[2] == dices_taken_out[1]+1 and dices_taken_out[3] == dices_taken_out[2]+1 and dices_taken_out[4] == dices_taken_out[3]+1:
        smallS = True
        points = 30
    if smallS:
        scoreList[9] = points
        return 0
    else:
        return 1



def largestraight(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 9th element of list"""
    largeS = True
    dices_taken_out.sort()
    for i in range(len(dices_taken_out)-1):
        if dices_taken_out[i+1] != dices_taken_out[i] + 1:
            largeS = False
    if largeS:
        scoreList[10] = 40
        return 0
    else:
        return 1



def yahtzee(dices_taken_out, scoreList):
    """takes in dices_taken_out and scoreList of a player. Adds the points to 10th element of list
        Also if there is another occurrence of yahtzee it adds 1 to the last element of the scoreList"""
    yatz = True
    dices_taken_out.sort()
    for i in range(len(dices_taken_out) - 1):
        if dices_taken_out[i + 1] != dices_taken_out[i]:
            yatz = False
    if yatz and yahtCount[0] == 0:
        scoreList[11] = 50
        yahtCount[0] += 1
    elif yatz and yahtCount[0] > 0:
        scoreList[14] += 1



def chance(dices_taken_out, scoreList):
    """takes in dices_taken_out and scorelist of a player. Adds the points to 11th element of list"""
    count = 0
    dices_taken_out.sort()
    for i in range(len(dices_taken_out)):
        count += dices_taken_out[i]
    scoreList[12] = count

def selecting(dices_taken_out, scoreList):
    '''Takes in the user input on how they want to score the dice, calls appropriate function'''
    displaycard(scoreList)
    print(" ")
    valid = False
    while valid == False:
        where_to_score = int(input("How would you like to score your dice? (select number 1-13):"))
        if where_to_score == 1:
            if ones(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 2:
            if twos(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 3:
            if threes(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 4:
            if fours(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 5:
            if fives(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 6:
            if six(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 7:
            if threeofakind(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 8:
            if fourofakind(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 9:
            if fullhouse(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 10:
            if smallstraight(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 11:
            if largestraight(dices_taken_out, scoreList1) == 0:
                valid = True
        elif where_to_score == 12:
            yahtzee(dices_taken_out, scoreList1)
            valid = True
        elif where_to_score == 13:
            chance(dices_taken_out, scoreList1)
            valid = True



def getTotal(scoreList):
    """Takes in the list of a players scores, output: returns the total score"""
    total = 0
    bonusTF = 0
    for i in range(len(scoreList)-1):
        total += int(scoreList[i])
    total += (int(scoreList[-1])*100)
    for i in range(6):
        bonusTF += int(scoreList[i])
    if bonusTF >= 63:
        total += 35
    return total


def yahtzeegame(amount):
    '''Rolls dice for user, prints menu options, takes in input for rolls and menu selection'''
    rollnum = 0
    dices_taken_out = []
    dicerolled = dices(amount)
    amount_taken_out = 0
    for d in range(3):
        if amount_taken_out == 5:
            print("No more dices able to be taken out")
            break
        dicerolled = dices(amount)
        if rollnum == 0: # roll 1
            # Menu options
            while True:
                ans = input("\nMENU OPTIONS\nInstructions [I]\nScoring Instructions [Z]\nCurrent score [S]\nShow Score Card [C]"
                            "\nQuit Game [Q]\nPlay Next Turn [X]\nEnter:")
                if ans.lower() == 'x':
                    break
                elif ans.lower() == 'i':
                    displayinstruction()
                elif ans.lower() == 'z':
                    displayscoring()
                elif ans.lower() == 's':
                    print("\nCURRENT SCORE:", getTotal(scoreList1))
                elif ans.lower() == 'q':
                    print("\nQuitting Game...")
                    sys.exit()
                elif ans.lower() == 'c':
                    displaycard(scoreList1)
            print("\nROLL 1:")
        if rollnum == 1: # roll 2
            print("\nROLL 2:")
        if rollnum == 2: # roll 3
            print("\nROLL 3:")
        print(dicerolled)
        asking = int(input("How many dices do you wish to keep"))
        if asking == len(dicerolled):
            rollnum = 0
            break
        amount_taken_out += asking
        amount -= asking
        for k in range(asking):
            which_dice_to_remove = int(input("Which dice would you like to keep? "))
            dices_taken_out.append(dicerolled.pop(dicerolled.index(which_dice_to_remove)))
        rollnum += 1
    print()
    print()
    print(dicerolled+dices_taken_out, "are the dice you selected")
    return dicerolled + dices_taken_out

def displaycard(x):
    """ Takes in a list of players scores, Output: prints a score card with the appropriately filled in scores"""
    # instantiating variables
    UpPreTotal = 0
    upBonus = 0
    upTotal = 0
    yBonus = x[13] * 100
    lowTotal = 0

    # calculate the bonuses and totals
    for i in range(6):
        UpPreTotal += x[i]
    if UpPreTotal >= 63:
        upBonus = 35
    upTotal = upBonus + UpPreTotal
    for i in range(6, 13):
        lowTotal += x[i]
    lowTotal += yBonus

    # convert to strings for syntax purposes
    x = list(map(str, x))
    UpPreTotal = str(UpPreTotal)
    upBonus = str(upBonus)
    upTotal = str(upTotal)
    yBonus = str(yBonus)
    lowTotal = str(lowTotal)
    gTotalstr = str(getTotal(x))

    print("                     |⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|", "|  ****LOWER*****   |SCORE|")
    print("|***UPPER*** |SCORE|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(7) 3 OF A KIND    |", x[6].rjust(3), "|")
    print("|(1) ONES    |", x[0].rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(8) 4 OF A KIND    |", x[7].rjust(3), "|")
    print("|(2) TWOS    |", x[1].rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(9) FULL HOUSE     |", x[8].rjust(3), "|")
    print("|(3) THREES  |", x[2].rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(10) SMALL STRAIGHT|", x[9].rjust(3), "|")
    print("|(4) FOURS   |", x[3].rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(11) LRGRE STRAIGHT|", x[10].rjust(3), "|")
    print("|(5) FIVES   |", x[4].rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(12) YAHTZEE       |", x[11].rjust(3), "|")
    print("|(6) SIXES   |", x[5].rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|(13) CHANCE        |", x[12].rjust(3), "|")
    print("|TOTAL       |", UpPreTotal.rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|YAHTZEE BONUS      |", x[13].rjust(3), "|")
    print("|BONUS       |", upBonus.rjust(3), "|", "|                   |⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|                   |", yBonus.rjust(3), "|")
    print("|UPPER TOTAL |", upTotal.rjust(3), "|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|⎻⎻⎻⎻⎻|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|")
    print("|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|", "|LOWER TOTAL        |", lowTotal.rjust(3), "|", "|GRAND TOTAL|", gTotalstr.rjust(3),
          "|")
    print("                     |⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|", "|⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻|")


# prints initial instructions
displayinstruction()
displayscoring()

# plays 13 turns
for i in range(13):
    selecting(yahtzeegame(amount), scoreList1)
displaycard(scoreList1)

# displays the game results
img=mpimg.imread('gameover.jpg')
imgplot = plt.imshow(img)
plt.show()
print("\n\nGame Complete!")
print("⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")
print("Player Score:", getTotal(scoreList1))
print("⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻")



