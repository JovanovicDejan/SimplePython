n = int(input("Enter a number: "))
sum = 0
const = n
if n < 0:
    n = -n
while n > 0:
    last_digit = n % 10
    sum += last_digit
    n = n // 10

if n % sum == 0:
    print(f"Number {const} can be devided by {sum} ")
else:
    print(f"Number {const} cant be devided by {sum} ")