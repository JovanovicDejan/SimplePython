#Count the number of the days depends on month and year, also checking if years is leap or not

year = int(input("Enter a year: "))
month = int(input("Enter a number of month from 1 to 12: "))

while month < 1 or month > 12:
    print("You need to enter valide number 1 or 12! ")
    month = int(input("Enter a number of month from 1 to 12: "))
if month == 1:
    print("January - 31 days")
elif month == 2:
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("It's a leap year, Febrauray - 29 days") 
    else:
        print("February - 28 days")
elif month == 3:
    print("March - 31 days")
elif month == 4:
    print("April - 30 days")
elif month == 5:
    print("May - 31 days")
elif month == 6:
    print("June - 30 days")
elif month == 7:
    print("July - 31 days")
elif month == 8:
    print("August - 31 days")
elif month == 9:
    print("September - 30 days")
elif month == 10:
    print("October - 31 days")
elif month == 11:
    print("November - 30 days")
elif month == 12:
    print("December - 31 days")