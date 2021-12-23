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
        

product1 = Product("Mars", 30)
product2 = Product("Chocolate", 100)
list_of_products = [product1,product2]
catalog1 = Catalog("Sweet",list_of_products)
product3 = Product("Snickers", 50)
catalog1.add_new_product(product3)
print(catalog1)