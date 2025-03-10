# Ask user to input 10 numbers 
# Print the length of all odd numbers

num = []

for i in range (1, 11):
    num = float(input(f'Input number {i}: '))
    if num % 2 == 0:
        odd.append(num)

