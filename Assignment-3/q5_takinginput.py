print("------------ SOLUTION 5 ------------")
print("TO GET PATTERN IN QUESTION ENTER 6 ELSE ENTER ANY NUMBER b/w 1,13")
while(True):
    n=int(input("Enter number of columns (From 1-13) ")) #Taking number of desired columns as input
    if n in range(1,14):
        break
    else:
        print("Error")
for i in range(0,n): # Loop for columns
    for j in range(0,i+1): #loop for spaces in each columns
        print(" "),
    for k in range(0,2*(n-i)-1): #loop for character in each columns
        print(chr((65+k))),
    print("") ## for going to next line after completing one row
