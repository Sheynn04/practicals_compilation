# Create a program that ask user to input 10 numbers. 
# Display all numbers that have duplicate.

num_list = []

for i in range(10):
    number = int(input(f"Input number {i+1}: "))
    num_list.append(number)

dupe_list = [num for num in num_list if num_list.count(num) > 1]
print(set(dupe_list))
        
        



