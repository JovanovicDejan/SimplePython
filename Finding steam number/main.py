n = int(input("Enter some whole number: "))
list_of_n = [str(x) for x in str(n)]
new_list_of_n = []
for digits in list_of_n:
    digits = int(digits)
    if digits % 2 == 0:
        digits += 1
    new_list_of_n.append(digits)

for num in new_list_of_n:
    print(num, end=" ")