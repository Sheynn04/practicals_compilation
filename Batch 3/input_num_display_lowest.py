# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the lowest number

while True:
    try:
        number = int(input("Input a number: "))
    except ValueError:
        exit()