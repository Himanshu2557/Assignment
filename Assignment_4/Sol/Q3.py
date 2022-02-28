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