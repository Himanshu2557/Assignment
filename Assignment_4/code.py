print('--------------------Question-1---------------------')

# Creation function to print steps to transfer disc from A to C
def TowerOfHanoi(n,source,destination,helper):

    # Base Case
    if n==0:
        return
# Firstly moving n-1 disc to B using C
    TowerOfHanoi(n-1,source,helper,destination)

# Moving top disc from A to C
    print("Move top disc from \033[1m%s\033[0m to \033[1m%s\033[0m" %(source,destination))

# Moving n-1 disc from B TO C Using A
    TowerOfHanoi(n-1,helper,destination,source)


# calling Function For 3 Disc
TowerOfHanoi(3,'A','C','B')


print('--------------------Question-2---------------------')
print('Using recucsion')

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
        print(" ",end=" ")
    for k in range(0,i+1):
        print(" %d " %(nCr(i,k)),end=" ") # print iCk ie. kth element of ith row
    print(" ") # For moving to next row


print("Using loops")
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
        print(" ",end=" ")
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
        print(" %d "%(factoriali/(factorialik*factorialk)),end=" ") # print iCk ie. kth element of ith row
print()

print('--------------------Question-3---------------------')
# Taking Input
n1=int(input("Enter FIRST INTEGER: "))
n2=int(input("Enter SECOND INTEGER: "))
print()

# remainder and quotient
rem=n1%n2
quot=int(n1/n2)

print("Quotient: %d" %quot)
print("Remainder: %d\n" %rem)

# Callable value
print("a. The quotient and reminder are a callable values.")
print(callable(quot))
print(callable(rem))

print("b. ",end="")
# Cheking zero value 
if(rem==0):
    if(quot==0):
        print("Both values are zero")
    else:
        print("One value is zero")
else:
    if(quot==0):
        print("One value is zero")

# Set
print("c. Filterd Values")
reqset=set()
for i in range (4,7):
    newrem=rem+i
    newquot=quot+i

    if(newrem>4):
        reqset.add(newrem)
    if(newquot>4):
        reqset.add(newquot)
print(reqset)

immutableset=frozenset(reqset)
print("d. Immutable set:",immutableset)

maximum=max(immutableset)
print("e. Maximum value in set is %d" %maximum)
print("f. Hash value: ", hash(maximum))


print('--------------------Question-4---------------------')
# Creating class
class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __del__(self):
        print("Object destroyed")
        
# Creating object
s1=student("Himanshu Goyal",21105029)
print("Object created")
print()
print(f"Name of student is {s1.name} and Roll No is {s1.rollno}")
print()

 # deleting object
del s1

print('--------------------Question-5---------------------')
#Creating class
class employee:
    # INITIALIZATION
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Function to print Info
    def info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary} ")
        print("")



# Creating objects
employee1=employee("Mehak",40000)
employee2=employee("Ashok",50000)
employee3=employee("Viren",60000)

# Printing employee info
employee1.info()
employee2.info()
employee3.info()

# Updating salary of Mehak
employee1.salary=70000

#Printing updated info of Mehak
print("Updated record of Mehak")
employee1.info()

# Deleting record of Viren
del employee3
print("Record of Viren deleted")


