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
