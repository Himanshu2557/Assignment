print("------------ SOLUTION 3 ------------")

list=[1,2,3,5,7,10,11] ## given list
Desired_list=[]
for i in list:
    tup=(i,i**2) # Making tuple with second number square of first
    Desired_list.append((i,i**2)) ## Adding tuple made above to the final list

print(Desired_list)

