#Average cost of products in store while cost greater then 0

#Using list
prices = []

while True:
    user_input = float(input("Enter a price of products: "))
    if user_input > 0:
        prices.append(user_input)
    if user_input <= 0:
        break

total = 0
for price in prices:
    total += price

if len(prices) == 0:
    print("Invalid number of products")

else:
    average_prices = total / len(prices)
    print(f"Average price in store {average_prices}$ ")


#Simple methods
# sum = 0
# i = 0
# while True:
#     user_input = float(input("Enter a price of products: "))
#     if user_input > 0:
#         sum += user_input
#         i = i + 1
#     if user_input <= 0:
#         break

# average_price = sum / i
# print(f"The average price of products in store {average_price}$")



# i = 0
# sum = 0
# n = 0
# while i <= 0:
#     if i >= 0:
#         user_input = float(input("Enter a price of products"))
#         if user_input < 0:
#             print("Invalid number")
#             exit(1)
#         sum += user_input
#         n = n + 1
#         if user_input <= 0:
#             break
# average_cost = sum / (n-1)
# print(f"The average cost of products in store {average_cost}$")