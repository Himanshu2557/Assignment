print("------------ SOLUTION 7 ------------")
# FIBONACCI SEQUENCE
while(True):
    n=int(input("Enter no. of terms till which Fibonacci sequence is to be printed: "))
    if(n>0):
        break
    else:
        print("error")
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


