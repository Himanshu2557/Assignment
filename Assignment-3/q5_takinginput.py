print("------------ SOLUTION 5 ------------")
print("For pattern in question enter 6")
n=int(input("Enter number of columns (From 0-13) ")) #Taking number of desired columns as input
for i in range(0,n): # Loop for columns
    for j in range(0,i+1): #loop for spaces in each columns
        print(" "),
    for k in range(0,2*(n-i)-1): #loop for character in each columns
        print(chr((65+k))),
    print("") ## for going to next line after completing one row
