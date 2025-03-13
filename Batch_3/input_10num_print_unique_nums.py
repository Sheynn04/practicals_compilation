# Ask the user to input 10 numbers
# Display all numbers without duplicates

raw_nums_list = []

for i in range(10):
    num_input = int(input(f'Input number {i+1}: '))
    raw_nums_list.append(num_input)

no_dupe_list = [num for num in raw_nums_list if raw_nums_list.count(num) == 1]
print (no_dupe_list)
    