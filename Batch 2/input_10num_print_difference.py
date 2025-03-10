# Ask user to input 10 numbers
# Get the first number
# Minus all the other number

result = 0

for i in range (10):
    num = int(input(f'Input number {i+1}: '))
    result = num[0] - sum(num[1:])
    print (result)
