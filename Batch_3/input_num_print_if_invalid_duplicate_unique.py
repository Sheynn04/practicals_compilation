# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

numbers = []
while True: 
    try:
        num = int(input("Input number: "))

    except ValueError:
        exit()

    if num in numbers:
        print("Duplicate")
    else:
        print("Unique")
        numbers.append(num)
    

        




    