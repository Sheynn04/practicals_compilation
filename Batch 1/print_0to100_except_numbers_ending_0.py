# For loop: print numbers 0 to 100 except numbers ending in 0

for i in range (0,100):
    if i % 10 == 0:
        continue
    print (i)