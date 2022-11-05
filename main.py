import random
from rules import rules
import requests

''' To do:
npc
play again?
remove special char from question
'''

questions_easy = "https://opentdb.com/api.php?amount=1&difficulty=easy&type=boolean"
questions_medium = "https://opentdb.com/api.php?amount=1&difficulty=medium&type=boolean"
questions_hard = "https://opentdb.com/api.php?amount=1&difficulty=hard&type=boolean"
questions_random = "https://opentdb.com/api.php?amount=1&type=boolean"
difficulty: str

mainloop = True
explain_rules = True
valid_numbers = "123456789"
numbers_taken = "0"
player1: str
player2: str

raster = '''
_ _|_ _|_ _
_ _|_ _|_ _
   |   |   
'''
raster_empty = raster
raster2 = ""
raster_positions = '''
_1_|_2_|_3_
_4_|_5_|_6_
 7 | 8 | 9 
'''

winning_positions = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
)


def check_winning_conditions():
    for item in winning_positions:
        if item[0] == "X" and item[1] == "X" and item[2] == "X":
            x_wins()
        elif item[0] == "O" and item[1] == "O" and item[2] == "O":
            o_wins()


def o_wins():
    print(raster)
    print(f"{player2} won")
    global mainloop
    mainloop = False


def x_wins():
    print(raster)
    print(f"{player1} won")
    global mainloop
    mainloop = False


def begin():
    global difficulty
    print(rules)
    difficulty = input("First, choose your difficulty: Easy, medium, hard.\n Leave empty for random. ").lower()

    if difficulty == "easy" or difficulty == "1" or difficulty == "e":
        difficulty = questions_easy
        difficulty_str = "Easy"
    elif difficulty == "medium" or difficulty == "2" or difficulty == "m":
        difficulty = questions_medium
        difficulty_str = "Medium"
    elif difficulty == "hard" or difficulty == "3" or difficulty == "h":
        difficulty = questions_hard
        difficulty_str = "Hard"
    else:
        difficulty = questions_random
        difficulty_str = "Random"
    print(f"{difficulty_str} questions were picked.")

    print("These are the possible positions. Choose wisely!")
    print(raster_positions)
    global player1
    player1 = input("Player 1 enter your name: ")
    global player2
    player2 = input("Player 2 enter your name: ")


def ask_a_question_player():
    print("Your question is:")
    response = requests.get(questions_easy)
    data = response.json()
    question = data.get("results")[0].get("question") + " True or false? "
    # now let's get rid of the json artifacts:
    question = question.split()
    question_no_artifacts = []
    for item in question:
        if "&quot;" in item:
            word = item.replace("&quot;", "'")
            question_no_artifacts.append(word)
        elif "&#039;" in item:
            word = item.replace("&#039;", "'")
            question_no_artifacts.append(word)
        else:
            question_no_artifacts.append(item)
    question = " ".join(question_no_artifacts)

    print(question)
    answer = input().capitalize()
    if answer == data.get("results")[0].get("correct_answer") or answer == str(data.get("results")[0].get("correct_answer"))[0]:
        return True
    else:
        return False



def play_a_round_player1():
    print("Correct!")
    global raster
    global raster2
    global numbers_taken
    print(raster)
    position = input(f"{player1}, choose your position! ")
    if position not in valid_numbers or position in numbers_taken:
        print("Invalid input! Too bad, that was your turn...")
    else:
        numbers_taken += position
        position = int(position)
        for item in winning_positions:
            for index, num in enumerate(item):
                if num == position:
                    item[index] = "X"
        for index, item in enumerate(raster_positions):
            if item == str(position):
                place_to_change = index
        for index, item in enumerate(raster):
            if index == place_to_change:
                raster2 += "X"
            else:
                raster2 += item
        raster = raster2
        raster2 = ""

def play_a_round_player2():
    print("Correct!")
    global raster
    global raster2
    global numbers_taken
    print(raster)
    position = input(f"{player2}, choose your position! ")
    if position not in valid_numbers or position in numbers_taken:
        print("Invalid input! Too bad, that was your turn...")
    else:
        numbers_taken += position
        position = int(position)
        for item in winning_positions:
            for index, num in enumerate(item):
                if num == position:
                    item[index] = "O"
        for index, item in enumerate(raster_positions):
            if item == str(position):
                place_to_change = index
        for index, item in enumerate(raster):
            if index == place_to_change:
                raster2 += "O"
            else:
                raster2 += item
        raster = raster2
        raster2 = ""



while mainloop:
    if explain_rules:
        begin()
        explain_rules = False
    else:
        question = ask_a_question_player()
        if question:
            play_a_round_player1()
            check_winning_conditions()
            if mainloop == False:
                break
        else:
            print("Wrong!")
            print(raster)
        question = ask_a_question_player()
        if question:
            play_a_round_player2()
            check_winning_conditions()
        else:
            print("Wrong!")
            print(raster)