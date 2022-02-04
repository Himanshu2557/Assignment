print("------------ SOLUTION 1 ------------")
str=input("Entered desired string ").lower().split() #Taking input and storing as list
count={}
if len(str)==1: #condition If only one word is entered
    str=str[0]
for x in str:
    if x in count:    
        count[x]+=1  
    else: #for word encountered first time
        count[x]=1
print("The count of:")
for j in count:
    print("\t'\033[1m%s\033[0m\' : %d"%(j,count[j]))


print("------------ SOLUTION 2 ------------")

day = int(input("Day - "))
Month = int(input("Month - "))
year=int(input("Year - ")) #Taking year as integer input

if year%4==0: 
    leap_year=1          #Checking for leap year
    if year%400==0:     #leap year is divisible by 4 but not by 100 but by 400
        leap_year=1
    elif year%100==0:
        leap_year=0 
else:
    leap_year=0


if Month in (1,3,5,7,8,10,12):  #number of days in month
    month_lenght=31
elif Month==2:    # for leap year number of days in feb = 29
    if leap_year:
        month_lenght=29
    else: 
        month_lenght=28
else:
    month_lenght=30


if day<month_lenght:
    day += 1
else:
    day=1     
    if Month==12:   #Changing month and or year if required
        Month=1
        year+=1
    else:
        Month+=1

print("Next Date is: \033[1m%d/\033[1m%d/\033[1m%d"%(day,Month,year))


print("------------ SOLUTION 3 ------------")

list=[1,2,3,5,7,10,11] ## given list
Desired_list=[]
for i in list:
    tup=(i,i**2) # Making tuple with second number square of first
    Desired_list.append((i,i**2)) ## Adding tuple made above to the final list

print(Desired_list)


print("------------ SOLUTION 4 ------------")

letter_grade={4:"D",5:'C',6:'C+',7:'B',8:'B+',9:'A',10:'A+'}  # Dictonary with key as grade and letter as value

performance= dict(zip(letter_grade.keys(),["Poor","Below Average","Average","Good","Very Good","Excellent","Outstanding"])) 
# dict fot performence by using keys from letter_grade and zippiing it with values written

while(True):
    grade=int(input("Enter grade (between 4 and 10): "))  #Taking  integer Input
    if grade in range(4,11):
        break
    else:
        print("Error")

if grade in range(4,11): ## Checking condition
    print("Your Grade is %s and %s" %(letter_grade[grade],performance[grade]))
else:
    print("Error")


print("------------ SOLUTION 5 ------------")
print("For pattern in question enter 6")
n=int(input("Enter number of columns (From 0-13) ")) #Taking number of desired columns as input
for i in range(0,n): # Loop for columns
    for j in range(0,i+1): #loop for spaces in each columns
        print(" "),
    for k in range(0,2*(n-i)-1): #loop for character in each columns
        print(chr((65+k))),
    print("") ## for going to next line after completing one row


    print("------------ SOLUTION 6 ------------")
next_student="Y"
details={} #empty dict to contain SID and name
name=[] # list of names
SID=[] # list of SID
while True:          #taking SID and name as input
    name.append(input("Enter name of student "))
    SID.append(int(input("Enter SID of student ")))
    details=dict(zip(SID,name))     #zip sid and name to form dict
    next_student=input("Do you want to enter student (Y/N) ") #asking to continue loop
    if next_student=='N':
        break

print("-->A")
print(details)

print("-->B")
print("Sorted dictionary using names")
sorted_name_dict={}
sorted_name=sorted(name) # list to conatin sorted name
for i in sorted(details.values()):
    for key,value in details.items():
        if value == i:
            sorted_name_dict[key]=value
print(sorted_name_dict)

print("-->C")
print("Sorted dictonary using SID's")
sorted_SID_dict={}
for i in sorted(details.keys()): 
    for key,value in details.items():
        if key ==i:
            sorted_SID_dict[key]=value
print(sorted_SID_dict)

print("-->D")
print(details[int(input("Enter student SID "))]) #searching name using SID in dict



print("------------ SOLUTION 7 ------------")
# FIBONACCI SEQUENCE
n=int(input("Enter no. of terms till which Fibonacci sequence is to be printed "))
first_term=0  # Initial terms for Sequnece
second_term=1
sum=0.0
for i in range (0,n):   
    sequnece=first_term+second_term # Adding previoud two numbers
    print(first_term)
    first_term=second_term  #updating first term to next term
    second_term=sequnece    #updating second term to next term
    sum+=first_term      # Sum of all terms of series
print(("Average Of sequence is %f" %(sum/n)))


print("------------ SOLUTION 8 ------------")
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

print("-->A")
set4=(set1^set2)  #Taking symmetric difference
print(set4)

print("-->B")
set5=((set1|set2|set3)-((set1&set2)|(set2&set3)|(set3&set1)))#difference of union of 3 sets with elements that occour in atleast two set
print(set5)

print("-->C")
set6=(set1&set2)^(set2&set3)^(set1&set3) #Taking intersection of 2 set to find elements common two set
print(set6)                #taking symmetric difference to remove elements in all three sets by removing duplicating term          
print("-->D")
set7=(set(range(1,11))-set1) #converting range to set and removing set1 elemnts from it
print(set7)

print("-->E")
set8=(set(range(1,11))-(set1|set2|set3))#converting range to set and removing all elements that are in 3 sets from range set
print(set8)
