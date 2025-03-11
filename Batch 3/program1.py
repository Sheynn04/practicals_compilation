# Ask user to input 10 numbers
# Display all numbers without duplicates

non_dupe_nums = []

for i in range(10):
    num_input = int(input(f'Input number {i+1}: '))
    if num_input != non_dupe_nums:
        non_dupe_nums.append(num_input)

print(non_dupe_nums)