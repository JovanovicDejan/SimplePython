#Clear the last zero,s in number

n = int(input("Enter whole number: "))

if n > 0:                   #Chek if n greater then 0
    for i in range(n):      #Using foor loop to itterate 
        last_digit = n % 10     #get last digit using %
        if last_digit == 0:     #Check if last equals to 0
            n = n // 10         #if last digit equals to 0 , remove 0 by using //
    print(n)

if n < 0:
    for j in range(n, -1):
        last_digit = n % 10
        if last_digit == 0:
            n = n // 10
    print(n)


#Simple if statement 
# if n <  0:
#     positive = True
#     n = -n
# else:
#     positive = False
# while n % 10 == 0:
#     n = n // 10
# if positive:
#     print(-n)
# else:
#     print(n)
