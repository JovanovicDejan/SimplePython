n = int(input("How many products is in store? "))
list_of_prices = []
for i in range(n):
    user_input = float(input(f"Enter price of {i+1} product: "))
    list_of_prices.append(user_input)

current_lowest_prices = list_of_prices[0]

for price in list_of_prices:
    if price < current_lowest_prices:
        current_lowest_prices = price
print(current_lowest_prices)