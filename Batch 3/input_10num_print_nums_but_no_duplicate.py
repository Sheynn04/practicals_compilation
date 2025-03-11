# Ask the user to input 10 numbers
# Print all the numbers including ones with duplicates but only print them once

raw_nums_list = []

for i in range(10):
    num_input = int(input(f'Input number {i+1}: '))
    raw_nums_list.append(num_input)

print(raw_nums_list)

