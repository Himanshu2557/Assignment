#Answer 3
print("\n\nAnswer 3.")

int1, int2 = map(int,input("Enter 2 numbers: ").split())

quo = int1 // int2
rem = int1 % int2

print(f"The quotient is {quo} and reminder is {rem}")

#part a
print("a. The quotient and reminder is a callable value.")
print(callable(quo))
print(callable(rem))

#part b
if quo == 0:
    print("b. The quotient is zero")
if rem == 0:
    print("b. The reminder is zero")
if quo != 0 and rem != 0:
    print("b. All the values are non zero")

#part c
clist = (quo , rem) + (4, 5, 6)

result = []
for i in range(len(clist)):
    if clist[i] < 5:
        result.append(clist[i])
print(f"c. Filtered out numbers: {result}")

#part d
setresult = set(result)
print("d. Set:",setresult)

#part e
setfrozen = frozenset(setresult)
print("e. Immutable set:",setfrozen)

#part f
print("f. Hash value of the max value from the above set:", hash(max(setfrozen)))