import random
from rules import rules

mainloop = True
explain_rules = True

raster = '''
_ _|_ _|_ _
_ _|_ _|_ _
   |   |   
'''

raster_positions = '''
_1_|_2_|_3_
_6_|_5_|_4_
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
    print("X won")

def x_wins():
    print("O won")

def begin():
    explain_rules = False
    print(rules)
    print("These are the possible positions. Choose wisely!")
    print(raster_positions)


while mainloop:
    if explain_rules:
        begin()
    else:
        break