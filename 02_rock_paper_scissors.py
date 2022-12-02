points = 0

with open(file="02_rock_paper.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')

        if line[0] == 'A' and line[2] == 'X':
            points += (1 + 3)
        elif line[0] == 'B' and line[2] == 'Y':
            points += (2 + 3)
        elif line[0] == 'C' and line[2] == 'Z':
            points += (3 + 3)
        elif line[0] == 'A' and line[2] == 'Y':
            points += (2 + 6)
        elif line[0] == 'A' and line[2] == 'Z':
            points += (3 + 0)
        elif line[0] == 'B' and line[2] == 'Z':
            points += (3 + 6)
        elif line[0] == 'B' and line[2] == 'X':
            points += (1 + 0)
        elif line[0] == 'C' and line[2] == 'X':
            points += (1 + 6)
        elif line[0] == 'C' and line[2] == 'Y':
            points += (2 + 0)

print(points)