# Create a program that ask user to input 10 numbers. 
# Display all numbers that have duplicate.

num_list = []
dupe_list = []
for i in range(10):
    number = int(input(f"Input number {i+1}: "))
    num_list.append(number)

    if number in num_list:
        dupe_list.append(number)

print(dupe_list)
        



