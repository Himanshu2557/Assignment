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
