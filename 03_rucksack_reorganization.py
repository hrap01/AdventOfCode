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

with open(file="03_rucksack_reorganization.txt", mode='r', encoding='utf-8') as f:
    sum_of_values = 0
    check = []
    check_2 = []
    for line in f:
        line = line.rstrip('\n')
        break_out_flag = False
        check.append(line)
        first_part = slice(0, int(len(line)/2))
        second_part = slice(int(len(line)/2), len(line))
        first_half = line[first_part]
        second_half = line[second_part]
        assert len(first_half) == len(second_half)

        for i in range(0, len(first_half)):
            for j in range(0, len(second_half)):
                if first_half[i] == second_half[j]:
                    value = first_half[i]
                    sum_of_values += letters_values[str(value)]
                    break_out_flag = True
                    break
            if break_out_flag:
                break



    print(sum_of_values)

