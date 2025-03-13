# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the highest number

num_list = []
while True:
    try:
        number = int(input("Input number:"))
        num_list.append(number)

    except ValueError:
        exit()
