from collections import Counter

with open(file="06_tuning_trouble.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        for i in range(0, len(line)):
            word = []
            for i in range(i, i+14):
                word.append(line[i])
            freq = Counter(word)
            if (len(freq) == len(word)):
                print(i+1)
                exit()
            else:
                pass
