print("------------ SOLUTION 8 ------------")
set1= {1, 2, 3, 4, 5}
set2= {2, 4, 6, 8}
set3= {1, 5, 9, 13, 17}

print("-->A")
set4=(set1^set2)  #Taking symmetric difference
print(set4)

print("-->B")
set5=set1^set2^set3 #Symmetric difference of all 3 sets
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