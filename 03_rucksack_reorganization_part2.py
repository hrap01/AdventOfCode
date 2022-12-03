letters_values = {'a': 1,
                  'b': 2,
                  'c': 3,
                  'd': 4,
                  'e': 5,
                  'f': 6,
                  'g': 7,
                  'h': 8,
                  'i': 9,
                  'j': 10,
                  'k': 11,
                  'l': 12,
                  'm': 13,
                  'n': 14,
                  'o': 15,
                  'p': 16,
                  'q': 17,
                  'r': 18,
                  's': 19,
                  't': 20,
                  'u': 21,
                  'v': 22,
                  'w': 23,
                  'x': 24,
                  'y': 25,
                  'z': 26,
                  'A': 27,
                  'B': 28,
                  'C': 29,
                  'D': 30,
                  'E': 31,
                  'F': 32,
                  'G': 33,
                  'H': 34,
                  'I': 35,
                  'J': 36,
                  'K': 37,
                  'L': 38,
                  'M': 39,
                  'N': 40,
                  'O': 41,
                  'P': 42,
                  'Q': 43,
                  'R': 44,
                  'S': 45,
                  'T': 46,
                  'U': 47,
                  'V': 48,
                  'W': 49,
                  'X': 50,
                  'Y': 51,
                  'Z': 52}
lines = []
with open(file="03_rucksack_reorganization.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        lines.append(line)

sum_of_values = 0
i=0

while i <= len(lines)-3:
    break_out_flag = False
    for j in range(0, len(lines[i])):
     for k in range(0, len(lines[i + 1])):
         for l in range(0, len(lines[i + 2])):
             if lines[i][j] == lines[i + 1][k] == lines[i + 2][l]:
                value = lines[i][j]
                sum_of_values += letters_values[str(value)]
                break_out_flag = True
                i += 3
                break
         if break_out_flag:
             break
     if break_out_flag:
         break


print(sum_of_values)





