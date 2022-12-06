from collections import Counter

with open(file="06_tuning_trouble.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        for i in range(0, len(line)):
            word = []
            word.append(line[i])
            word.append(line[i+1])
            word.append(line[i + 2])
            word.append(line[i + 3])
            freq = Counter(word)
            if (len(freq) == len(word)):
                print(i+4)
                exit()
            else:
                pass
