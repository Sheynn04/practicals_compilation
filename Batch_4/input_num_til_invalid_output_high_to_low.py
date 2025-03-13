# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number from highest to lowest. 
# Clue: sort() function

num_list =[]
while True:
    try:
        numbers = int(input("Input numbers: "))
        num_list.append(numbers)
    except ValueError:
        num_list.sort(reverse=True)
        print(num_list)
        exit()
    