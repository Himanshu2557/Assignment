# Question 1
print("         Question-1 ")
a,b,c=input('Enter First Number\n'),input("Enter Second Number\n"),input("Enter Third Number\n")
a,b,c=int(a),int(b),int(c)
average=(a+b+c)/3
print('Average of numbers: ',average)


# Question 2
print("         Question-2 ")
Gross_Income=int(input("Enter your gross income: "))
Dependents=int(input("Enter Number of dependents: "))
standard_deducion=10000
Dependent_deduction=3000
tax_rate=0.20 #percent
taxable_income = Gross_Income - standard_deducion - (Dependent_deduction*Dependents)
tax=taxable_income*tax_rate
print("Your total tax:",tax,"$")


# Question 3
print("         Question-3 ")
print("[SID, Name, Gender, Course Name, CGPA]")
student=[21105029,"Himanshu",'M',"Intro to Computing",9.7]
print(student)


# Question 4
print("         Question-4 ")
marks=list(input("Enter Marks Of Students: ").split()) #taking input and converting in list
for i in marks:
    marks[marks.index(i)]=int(i)
marks.sort()
print(marks)


# Question 5
print("         Question-5 ")

color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Part A")
color.pop(4)
print(color)

color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("Part B")
color[3:5]=["Purple"]
print(color)
