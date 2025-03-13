# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

numbers = []
while True: 
    num = int(input("Input number: "))
    numbers.append(num)

    for unique_num in numbers:
        if numbers.count(unique_num) == 1:
            print('Unique')

    for dupe_num in numbers:
        if numbers.count(dupe_num) != 1:
            print('Duplicate')




    