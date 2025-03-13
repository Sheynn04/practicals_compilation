# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the average.
num_list = []
while True:
    try:
        numbers = int(input("Input number: "))
        num_list.append(numbers)
    except ValueError:
        exit()
