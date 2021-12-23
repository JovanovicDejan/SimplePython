#Multiples the number by every natrual number below it. Factorial

print("Count factoriel of a number")
user_input = int(input("Enter a number: "))

while user_input <= 0:
    print("Please enter a number higher than 0")
    user_input = int(input("Enter a number: "))


#Using for loop
factoriel = 1
for i in range(1, user_input+1):
    factoriel *= i
print(factoriel)


# Using while loop
fact = 1
while user_input > 0:
    fact *= user_input
    user_input -= 1

print(fact)
    