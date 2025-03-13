# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number from lowest to highest. Clue: sort() function

num_list = []
while True:
    
    try:
        number = int(input("Enter number: "))
        num_list.append(number)

    except ValueError:
        num_list.sort()
        print(num_list)
        exit()

    