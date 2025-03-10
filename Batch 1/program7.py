# Ask user to input 10 numbers
# Print the sum of all numbers

sum = 0

for i in range (1, 11):
    num = float(input(f'Input number {i}: '))
    sum += num

print(sum)
    