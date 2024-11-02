try:
    #enter the number of rows for the diamond shape
    row_num = int(input("enter number of rows: "))

    # Check if the entered number is positive
    if row_num <= 0:
        print("INVALID:The number should be positive")

    #The top half of the diamond
    for i in range(1, row_num + 1):

        for j in range(row_num - i + 1): #Print spaces before the stars to center the diamond
            print(" ", end = '')

        for j in range (2 * i - 1): # Print the stars for the current row
            print("*", end = '')

        print() # Move to the next line after completing the row

    #The bottom half of the diamond
    for i in range (row_num - 1, 0, -1):

        for j in range (row_num - i + 1):
            print(" ", end = '')

        for j in range (2 * i - 1):
            print("*", end = '')

        print()

except ValueError:
    # Handle the case where the input is not a valid integer
    print("INVALID:Enter only a number")
