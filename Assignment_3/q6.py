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
print("Name of student is %s" %details[int(input("Enter student SID "))]) #searching name using SID in dict
