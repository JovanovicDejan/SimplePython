from author import Author   #From author file importing Author class

class Book:
    __title:str
    __author:Author #Create private author value type Author because we gave all atributes that Author class have 
    score:int

    def __init__(self,title:str,author:Author, score:int) -> None:
        self.__title = title
        self.__author = author
        self.score = score
    
    @property
    def title(self):
        return self.__title
    
    
    @property
    def author(self):
        return self.__author
    
    @title.setter
    def title(self, new_title):
        self.__title = new_title

    @author.setter
    def author(self, new_author):
        self.__author = new_author
    
    def __str__(self) -> str:
        return f"Book: {self.title}, Score: {self.score} \n{self.author}"   #Using __str__ and return methods to print in terminal what we want to see similar to print()
        #f" {variable}" allow us to write inside " " and show variables that we want
    
def main():
    robert = Author("Robert", "Jordan", 1948)   #Create object from Inheritance class Author  
    daniel = Author("Daniel", "Suarez", 1964)
    iris = Book("The Iris light", robert, 9.5)
    freedom = Book("Freedom" , daniel, 9.1)
    print(iris)
    print(freedom)

main()

