# Ask user to input 10 numbers
# Get the first number
# Minus all the other number


num = [float(input(f"Enter number {i+1}: ")) for i in range(10)]
result = num[0] - sum(num[1:])
print (result)
