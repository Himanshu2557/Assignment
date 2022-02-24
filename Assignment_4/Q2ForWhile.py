# Taking Input and ensuring it is greater than 0
while True:
    n=int(input("Enter Number of rows: "))
    if n<0:
        print("ERROR rows should be greator than zero")  #if n<0 print error
    else:
        break
# printng the sequence
for i in range(0,n):  # Loop for iteration rows
    for j in range(0,n-i): # Loop for printng space before first elemrent of ith row
        print(" "),
    for k in range(0,i+1): # Loop for printing element if ith row
        factoriali=1
        factorialk=1
        factorialik=1
        for m in range(1,i+1): #finding factorial of i
            factoriali*=m
        for m in range(1,k+1): #finding factorial of k
            factorialk*=m
        for m in range(1,(i-k)+1): #finding factorial of (i-k)
            factorialik*=m
        print(" %d "%(factoriali/(factorialik*factorialk))), # print iCk ie. kth element of ith row

    print(" ")