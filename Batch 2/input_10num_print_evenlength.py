# Ask user to input 10 numbers
# Display the length of all the even numbers they inputted

even = []

for i in range (10):
    num = float(input(f'Enter number {i+1}: '))
    if num % 2 == 0:
        even.append(num)
print(len(even))