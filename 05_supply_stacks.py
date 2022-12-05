from collections import deque

stack_1 = deque(['B', 'Z', 'T'])
stack_2 = deque(['V', 'H', 'T', 'D', 'N'])
stack_3 = deque(['B', 'F', 'M', 'D'])
stack_4 = deque(['T', 'J', 'G', 'W', 'V', 'Q', 'L'])
stack_5 = deque(['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'])
stack_6 = deque(['V', 'Z', 'Q', 'G', 'H', 'F', 'S'])
stack_7 = deque(['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'])
stack_8 = deque(['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'])
stack_9 = deque(['M', 'Q', 'L', 'F', 'D', 'S'])



with open(file="05_supply_stacks.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        move, number, from_, original_stack, to_, final_stack = line.split(' ')
        original_stack = 'stack_' + original_stack
        final_stack = 'stack_' + final_stack
        i = 1
        while i <= int(number):
            a = eval(original_stack).pop()
            eval(final_stack).append(a)
            i += 1

print(f"{stack_1} \n {stack_2} \n {stack_3} \n {stack_4} \n {stack_5} \n {stack_6} \n {stack_7} \n {stack_8} \n {stack_9}")