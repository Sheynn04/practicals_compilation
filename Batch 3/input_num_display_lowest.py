# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the lowest number

num_list = []
while True:
    try:
        number = int(input("Input a number: "))
        num_list.append(number)
    except ValueError:
        print(min(num_list))
        exit()

