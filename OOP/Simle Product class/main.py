class Product:
    __name:str
    __cost:float

    def __init__(self, name:str, cost:float) -> None:
        self.__name = name
        self.__cost = cost
    
    def get_name(self):
        return self.__name
    
    def get_cost(self):
        return self.__cost
    
    def set_name(self,new_name):
        self.__name = new_name
    
    def set_cost(self,new_cost):
        self.__cost = new_cost
    
    def __str__(self) -> str:
        output = f"Name of product: {self.__name}\n"
        output += f"Product cost: {self.__cost} \n"
        return output
    
class Catalog:
    __name_of_catalog:str
    __list_of_products = list[Product]

    def __init__(self, name_of_catalog:str, list_of_products:list) -> None:
        self.__name_of_catalog = name_of_catalog
        self.__list_of_products = list_of_products


    def get_name_of_catalog(self):
        return self.__name_of_catalog


    def get_list_of_products(self):
        return self.__list_of_products


    def set_name_of_catalog(self,new_name_of_catalog):
        self.__name_of_catalog = new_name_of_catalog


    def set_new_list_of_products(self, new_list_of_products):
        self.__list_of_products = new_list_of_products
    
    
    def add_new_product(self,new_product:Product):
        self.__list_of_products.append(new_product)
    

    def find_product(self,name_of_product):
        for products in self.__list_of_products:
            if products.get_name() == name_of_product:
                return products

    def find_product_with_heighest_price(self):
        product_with_heighest_price = self.__list_of_products[0].get_cost()
        heighest_cost_product = self.__list_of_products[0]

        for product in self.__list_of_products:
            current_heighest_price = product.get_cost()
            if current_heighest_price > product_with_heighest_price:
                product_with_heighest_price = current_heighest_price
                heighest_cost_product = product
            
        return f"Product with heighest price:\n{heighest_cost_product}"

    
    def sum_of_all_products(self):
        sum = 0
        for product in self.__list_of_products:
            sum += product.get_price()
        return sum

    
    def average_price(self):
        total = 0
        counter = 0
        for product in self.__list_of_products:
            total += product.get_price()
            counter += 1
        average = total / counter
        return f"Average price of products: {average}"


    def __str__(self) -> str:
        output = f"Catalog: {self.__name_of_catalog} \n"
        for product in self.__list_of_products:
            output += f"{product} \n"
        
        return  output
        

# product1 = Product("Mars", 30)
# product2 = Product("Chocolate", 100)
# list_of_products = [product1,product2]
# catalog1 = Catalog("Sweet",list_of_products)
# product3 = Product("Snickers", 50)
# catalog1.add_new_product(product3)
# print(catalog1)

number_of_catalog = int(input("How many catalag do you want to create? "))  
list_of_catalog = []            #Create list of catalog so we can work with it easier
for i in range(number_of_catalog):     
    catalog_name = input("What is the name of catalog: ")       #For each i create new catalog_name
    number_of_products = int(input("How many products do you want to add: "))   #After next loop is ended creat new catalog with different number of products
    list_of_products = []                                       #Create list of products each time for j is ended it create's empty list of products for next catalog
    for j in range(number_of_products):
        name_of_product = input("Name of product: ")
        cost = float(input("What is price of product: "))
        new_product = Product(name_of_product,cost)         #After user input name and cost of product, we are ready to create a new product with he's parameters
        list_of_products.append(new_product)                #Add each product to list of product 
    new_catalog = Catalog(catalog_name,list_of_products)    #After we end with J loop, we are ready to create a new catalog because we have all parameters for it
    list_of_catalog.append(new_catalog)                     #Aftre create new catalog, we can add it in list of catalogs

for catalog in list_of_catalog:                                #For each catalog in list of catalog's , print each catalog one by one
    print(catalog)