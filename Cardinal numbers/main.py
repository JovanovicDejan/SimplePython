#Find the divisor of numbers
n = int(input("Enter a number: "))

if n <= 1:
    while n <= 1:
        print("Please enter a number higher than 0")
        n = int(input("Enter a number: "))
for i in range(2,n):
    if n % i == 0:
        print(i, end=" ")
