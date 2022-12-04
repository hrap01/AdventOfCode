counter = 0

with open(file="04_camp_cleanup.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        first_set, second_set = line.split(',')
        first_set_one, first_set_two = first_set.split('-')
        second_set_one, second_set_two = second_set.split('-')
        first_set_value, second_set_value = [], []

        for i in range(int(first_set_one), int(first_set_two)+1):
            first_set_value.append(i)

        for i in range(int(second_set_one), int(second_set_two)+1):
            second_set_value.append(i)

        first_set_value_set = set(first_set_value)
        second_set_value_set = set(second_set_value)

        if first_set_value_set.issubset(second_set_value_set) or second_set_value_set.issubset(first_set_value_set):
            counter += 1

print(counter)
