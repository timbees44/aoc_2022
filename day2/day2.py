"""
A = Rock
B = Paper
C = Sissors
X = Rock
Y = Paper
Z = Sissors

Rock = 1
Paper = 2
Sissors = 3
Lose = 0
Draw = 3
Win = 6

PUZZLE ONE LAYOUT
A,X = 4
A,Y = 8
A,Z = 3
B,X = 1
B,Y = 5
B,Z = 9
C,X = 7
C,Y = 2
C,Z = 6

"""
f = open("input.txt", "r")

# Round 1
# Score dict
score = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6
        }

total = 0

# iterate and sum
for line in f.readlines():
    if line[:3] in score.keys():
        total += score[line[:3]]

print(f"Total if X,Y,Z = Rock, Paper, Scissors: {total}")

#Round 2
"""
X = Lose
Y = Draw
Z = Win
"""

score_2 = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7
        }

total_2 = 0

f.seek(0, 0)
for line in f.readlines():
    if line[:3] in score_2.keys():
        total_2 += score_2[line[:3]]

print(total_2)

print(f"Total if X,Y,Z = Lose, Draw, Win: {total_2}")

f.close()

