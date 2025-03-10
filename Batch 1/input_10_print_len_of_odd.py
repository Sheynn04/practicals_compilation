# Ask user to input 10 numbers 
# Print the length of all odd numbers

odd = []

for i in range (10):
    num = float(input(f'Input number {i+1}: '))
    if num % 2 != 0:
        odd.append(num)

print(len(odd))