#taking user input's to get degreed of number

# total = x**n      #We can use operator for degreeds
# print(f"The {n} degreed of {x} is {total}")

def degreed(x,n):
    const = x
    if n > 1:
    #While loop
    # while n > 1:
    #     x = const * x
    #     n = n - 1
    
    #For loop
        for i in range(1,n):
            x = const * x
        return x
    else:
        return 1

x = float(input("Enter a number: "))
n = int(input("Enter a degree: "))

total = degreed(x,n)
print(f"The {n} degreed of {x} is {total} ")
