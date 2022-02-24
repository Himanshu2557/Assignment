class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

s1=student("Himanshu Goyal",21105029)
del s1
s2=student(input("Enter Name: "),int(input("Enter RollNo: ")))