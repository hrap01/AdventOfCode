stack_1 = ['B', 'Z', 'T']
stack_2 = ['V', 'H', 'T', 'D', 'N']
stack_3 = ['B', 'F', 'M', 'D']
stack_4 = ['T', 'J', 'G', 'W', 'V', 'Q', 'L']
stack_5 = ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M']
stack_6 = ['V', 'Z', 'Q', 'G', 'H', 'F', 'S']
stack_7 = ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W']
stack_8 = ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M']
stack_9 = ['M', 'Q', 'L', 'F', 'D', 'S']



with open(file="05_supply_stacks.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line = line.rstrip('\n')
        move, number, from_, original_stack, to_, final_stack = line.split(' ')
        original_stack = 'stack_' + original_stack
        final_stack = 'stack_' + final_stack
        a = eval(original_stack)[-int(number):]
        del eval(original_stack)[len(eval(original_stack))-int(number):]
        for i in range(0, int(number)):
            eval(final_stack).append(a[i])

print(f"{stack_1} \n {stack_2} \n {stack_3} \n {stack_4} \n {stack_5} \n {stack_6} \n {stack_7} \n {stack_8} \n {stack_9}")