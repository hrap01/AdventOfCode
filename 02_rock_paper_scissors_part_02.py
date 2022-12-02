points = 0
# A rock 1
# B paper 2
# C scissors 3

# rock X 1 lose 0    lose A =
# paper Y 2 draw 3
# scissors Z 3 win  6

with open(file="02_rock_paper.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')

        if line[2] == 'X': # lose
            if line[0] == 'A':
                points += 3
            elif line[0] == 'B':
                points += 1
            elif line[0] == 'C':
                points += 2

        elif line[2] == 'Y': # draw
            if line[0] == 'A':
                points += (1 + 3)
            elif line[0] == 'B':
                points += (2 + 3)
            elif line[0] == 'C':
                points += (3 + 3)

        elif line[2] == 'Z': # win
            if line[0] == 'A':
                points += (2 + 6)
            elif line[0] == 'B':
                points += (3 + 6)
            elif line[0] == 'C':
                points += (1 + 6)

print(points)
