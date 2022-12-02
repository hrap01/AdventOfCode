calories_list = []
sum_of_calories = 0

with open(file="01_calories.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        if line != '':
            sum_of_calories += int(line)
        else:
            calories_list.append(sum_of_calories)
            sum_of_calories = 0


def bubble_sort(l):
    i = 0
    if l is not None:
        while i < (len(l) - 1):
            if l[i] >= l[i + 1]:
                i += 1
            else:
                back_value = 1
                for j in range(0, len(l) - back_value):
                    if l[j] < l[j + 1]:
                        l[j], l[j + 1] = l[j + 1], l[j]
                    back_value += 1
                    i = 0
    return l

bubble_sort(calories_list)
print(sum(calories_list[0:3]))
