r = int(input("enter number of rows: "))
#The top half of the diamond
for i in range(1, r + 1):
    for j in range(r - i):
        print(" ", end = '') 

    for j in range (1, i * 2):
        print("*", end = '')

    print() # Move to the next line after completing the row

# The bottom half of the diamond
for i in range (r - 1, 0, -1):
    for j in range (r - i):
        print(" ", end = '')

    for j in range (1, i * 2):
        print("*", end = '')

    print() 

    
    
         