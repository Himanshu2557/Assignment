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

    print(" ")

print('--------------------Question-3---------------------')
# Taking input
int1=int(input("Enter First Integer: "))

while(True):
    int2=int(input("Enter Second Integer: "))
    if int2!=0:
        break
    else:
        print("Divisor Cannot be Zero\n Pleade enter second integer again\n")
# DIVMOD
solution=divmod(int1,int2)
print(f"\nQuotient is {solution[0]} \nRemainder is {solution[1]}\n")

# Check callable or not
print("a. To Check whether the function is callable or not:")
call=callable(divmod)
print(call,end="")
if call == True:
    print(", Hence it is callable")
else:
    print(", Hence it is not callable")

# Cheking zero value 
if(solution[1]==0):
    if(solution[0]==0):
        print("b. Both values are zero")
    else:
        print("b. One value is zero")
else:
    if(solution[0]==0):
        print("b. One value is zero")
print()

# Filter value greater than 4
print("c. Filterd Values are")
allvalues=solution+(4,5,6)
filteredvalues=sorted(list(i for i in allvalues if i>4))
for i in filteredvalues:
    print(i,end=" ")
print()

# Converting to set datatype
print("\nd. Output in set Data type is",end=" ")
setdata = set(filteredvalues)
print(setdata)

# Making set immutable
immutableset=frozenset(setdata)
print("e. Immutable set:",immutableset)

# Finding maximum value and converting it into hash
maximum=max(immutableset)
print("f. Maximum value in set is %d" %maximum)
print("   Hash value: ", hash(maximum))


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


print('--------------------Question-6---------------------')

#inputting a word 
word = input("Enter the Word: ").lower()

#inputting a meaningful word with the exact same letters
testword = input("\nEnter a MEANINGFULL word to test your friendship: ").lower()

#defining dictionary to check if letters are same
def count_in_dict(word):
    count = {}
    list1 = list(word)
    
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

# checking same letter condition
if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")
else:
#shopkeeper to verify the word's meaning
    while True:
        ans = input("\nDoes the word makes sense?(y or n)\n").lower()

        if ans == 'y':
            print("The friends pass the friendship test!!\n")
            break
        elif ans == 'n':
            print("The word doesn't have a meaning, friendship is fake!!\n\n")
            break
        else:
            print("Invalid input, try again")

