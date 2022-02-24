# Function to find factorial of a number
def factorial(n): 
    if n==0:      #base case 0! = 1
        return 1
    return n*factorial(n-1)
# Function to find nCr
def nCr(n,r):
    return(factorial(n)/(factorial(r)*factorial(n-r)))  # nCr = n!/(r!*(n-r)!)

# Taking Input and ensuring it is greater than 0
while True:
    n=int(input("Enter Number of rows: "))
    if n<0:
        print("ERROR rows should be greator than zero")
    else:
        break

for i in range(0,n):
    for j in range(0,n-i):  # Loop for printng space before first elemrent of ith row
        print(" "),
    for k in range(0,i+1):
        print(" %d " %(nCr(i,k))), # print iCk ie. kth element of ith row
    print(" ") # For moving to next row