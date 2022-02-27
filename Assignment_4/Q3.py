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



    
