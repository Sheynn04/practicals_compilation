# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number from lowest to highest. Clue: sort() function

while True:
    try:
        number = int(input("Enter number: "))
    except ValueError:
        exit()

    