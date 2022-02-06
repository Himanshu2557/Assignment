print("------------ SOLUTION 2 ------------")

def leap_year(year=False):                                                                                
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

while True:
    day = int(input("Day - "))
    Month = int(input("Month - "))
    year = int(input("Year - "))
    if (day < 1) or (day > 31) or (Month < 1) or (Month > 12) or (year < 1800) or (year > 2025):                  #Condition for given constraints in the question
        print("Please use the given conditions for entering the current date\n1<=month<=12\n1<=day<=31\n1800<=year<=2025")
        continue
    if Month in (4,6,9,11) and day == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days\nEnter a valid date")
        continue
    elif Month == 2 and day >= 29:                                                                                 #Condition for no. of days in February
        if leap_year(year) and day != 29:
            print("The given month has only 29 days\n\Enter a valid date")
            continue
        elif not leap_year(year):
            print("The given month has only 28 days\nEnter a valid date")
            continue
    break



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

print("Next Date is: %d/%d/%d"%(day,Month,year))

