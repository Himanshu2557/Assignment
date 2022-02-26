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