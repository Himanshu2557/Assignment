print("------------ SOLUTION 2 ------------")

day = int(input("Day - "))
Month = int(input("Month - "))
year=int(input("Year - ")) #Taking year as integer input

if year%4==0: 
    leap_year=1          #Checking for leap year
    if year%400==0:     #leap year is divisible by 4 but not by 100 but by 400
        leap_year=1
    elif year%100==0:
        leap_year=0 
else:
    leap_year=0


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

print("Next Date is: \033[1m%d/\033[1m%d/\033[1m%d"%(day,Month,year))

