print('--------------------Question-3---------------------')
# Taking Input
n1=int(input("Enter FIRST INTEGER: "))
n2=int(input("Enter SECOND INTEGER: "))
print()

# remainder and quotient
rem=n1%n2
quot=int(n1/n2)

print("Quotient: %d" %quot)
print("Remainder: %d" %rem)
print()
# Cheking zero value 
if(rem==0):
    if(quot==0):
        print("Both values are zero")
    else:
        print("One value is zero")
else:
    if(quot==0):
        print("One value is zero")
print()
# Set
reqset=set()
for i in range (4,7):
    newrem=rem+i
    newquot=quot+i

    if(newrem>4):
        reqset.add(newrem)
    if(newquot>4):
        reqset.add(newquot)
print(reqset)
print()
        

immutableset=frozenset(reqset)

maximum=max(immutableset)
print("Maximum value in set is %d" %maximum)
print("Hash value: ", hash(maximum))



    
