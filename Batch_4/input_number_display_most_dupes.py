# Create a program that ask user to input a number, 
# continue asking until the user input is invalid. 
# Display the number with the most number of duplicate.

num_list = []

while True:

    try:
        number = int(input("Enter a number: "))
        num_list.append(number)

    except ValueError:
        most_duplicate_num = max(set(num_list), key=num_list.count)
        print(f"Most entered number: {most_duplicate_num}")
        exit()






    