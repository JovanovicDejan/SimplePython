#Take user's input and revers order of numbers

n = int(input("Enter number: "))

if n == 0:
    print(0)
elif n < 0:
    n = -n 
    while n > 0:
        last_digit = n % 10
        print(last_digit, end=" ")
        n = n // 10
