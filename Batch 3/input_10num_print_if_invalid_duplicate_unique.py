# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.

numbers = []
while True: 
    num = int(input("Input number: "))
    numbers.append(num)

    for indiv_num in numbers:
        if numbers.count(indiv_num) == 1:
            print('Unique')



    