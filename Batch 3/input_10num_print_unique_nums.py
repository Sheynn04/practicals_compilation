# Ask user to input 10 numbers
# Display all numbers without duplicates

nums_compile = []

for i in range(10):
    num_input = int(input(f'Input number {i+1}: '))
    nums_compile.append(num_input)

non_dupe_nums = list(set(nums_compile))
print(non_dupe_nums)
    