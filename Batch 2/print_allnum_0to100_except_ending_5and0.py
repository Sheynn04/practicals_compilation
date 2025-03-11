# Print all numbers from 0 to 100 except for the numbers ending in zero or five

for i in range(100):
    if i % 10 != 0 and i % 5 != 0:
        print(i)