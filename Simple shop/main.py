#WE have price, quantity and customer export , and we need to calculate how much money we need to give back to customer

price = float(input("Enter the price of product: "))
quantity = int(input("Enter the number of products: "))
customer_export = float(input("Enter customer export: "))

total = customer_export - (price * quantity)
if total < 0:
    print("The buyer need to hang more money! ")
else:
    print(f"Change for customer is {total}$")
