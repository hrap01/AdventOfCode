calories_list = []
sum_of_calories = 0
highest_calories = 0

with open(file="01_calories.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        if line != '':
            sum_of_calories += int(line)
        else:
            calories_list.append(sum_of_calories)
            sum_of_calories = 0

for calories in calories_list:
    if calories > highest_calories:
        highest_calories = calories

print(highest_calories)
