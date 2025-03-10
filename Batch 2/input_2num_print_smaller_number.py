# Ask user to input 2 numbers. 
# Print the smaller input 

num1 = float(input('Input 1st number: '))
num2 = float(input('Input 2nd number: '))

if num1 < num2:
    print (num1)
elif num2 < num1:
    print (num2)
else:
    exit()