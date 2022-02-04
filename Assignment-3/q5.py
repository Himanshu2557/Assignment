print("------------ SOLUTION 4 ------------")

string = "ABCDEFGHIJK" #Taking number of desired columns as input
for i in range(0,(len(string)//2)+1): # Loop for columns
    for j in range(0,(i+1)): #loop for spaces in each columns
        print(" ",end = '')
    for k in range(0,(len(string)-(2*i))): #loop for character in each columns
        print(string[k], end = '')
    print("") ## for going to next line after completing one row

