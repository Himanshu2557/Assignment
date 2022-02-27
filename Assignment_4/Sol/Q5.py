print('--------------------Question-5---------------------')
#Creating class
class employee:
    # INITIALIZATION
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Function to print Info
    def info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: {self.salary} ")
        print("")


# Creating objects
employee1=employee("Mehak",40000)
employee2=employee("Ashok",50000)
employee3=employee("Viren",60000)

# Printing employee info
employee1.info()
employee2.info()
employee3.info()

# Updating salary of Mehak
employee1.salary=70000

#Printing updated info of Mehak
print("Updated record of Mehak")
employee1.info()

# Deleting record of Viren
del employee3
print("Record of Viren deleted")


