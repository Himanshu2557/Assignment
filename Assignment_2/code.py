------------------------------------------------------------------------------------------
print("*************** Question 1 ******************")
input="Python is a case sensitive lanaguage"
print("a.")
print("Lenght of the string is: %s" %len(input))
print("b.")
print("The reversed string would be: %s" %input[::-1])
print("c.")
NewStr=input[12:26]
print("New string: %s" %NewStr)
print("d.")
replaced_input=input.replace("case sensitive","object oriented")
print("Replaced string is: %s"%replaced_input)
print("e.")
sub_str="a"
print("Index of first occurrence of substring \"a\" is: %s" %input.find("a") )
print("f.")
print("String without white spaces is: %s" %input.replace(" ",""))
------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------
print("*************** Question 2 ******************")
name="Himanshu Goyal"       #Assigning Variables
SID=21105029
department_name="ECE"
CGPA=9.8
print("""Hey, %s Here!
My SID is %s
I am from %s department and my CGPA is %s """ %(name,SID,department_name,CGPA))
------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------
print("*************** Question 3 ******************")
a=56
b=10
print("a...")
print("a & b = %d" % (a&b))
print("b...")
print("a | b = %d"%(a|b))
print("c...")
print("a ^ b = %d"%(a^b))
print("d...")
print("Left shifting a and b with 2 bits: a = %d b = %d"%(a<<2,b<<2))
print("e...")
print("Right shifting a with 2 bits and b with 4 bits: a = %d b = %d"%(a<<2,b<<4))
------------------------------------------------------------------------------------------



------------------------------------------------------------------------------------------
print("*************** Question 4 ******************")
input_numbers=input("Enter the numbers (in \" \"): ").split()
i=0
while i < len(input_numbers):
    input_numbers[i]=int(input_numbers[i])  #converting to integer
    i+=1 #increasing i by 1

print("The greatest number among the entered numbers is %s\n" % max(input_numbers))

#Question 5
print("*************** Question 5 ******************")
str=input("Enter desired string(in ' ') ")
if "name" in str:
    print("YES")
else:
    print("NO")
------------------------------------------------------------------------------------------
    
    
-------------------------------------------------------------------------------------------
print("*************** Question 6 ******************")
sides=input("Enter sides of triangles(in ' ') ").split()
sorted(sides)   # sorting
if int(sides[2])<(int(sides[1]) + int(sides[0])):   #checking condition
    print("YES")
else:
    print("NO")

---------------------------------------------------------------------------------------------
