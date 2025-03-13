# Ask user to input 10 numbers
# Print the sum of all numbers

sum = 0

for i in range(10):
    num = float(input(f'Input number {i+1}: '))
    sum += num

print(sum)
    