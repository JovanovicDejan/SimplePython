class Author:
    ___name:str
    __surname:str
    __birthYear:int

    def __init__(self, name:str, surname:str, birthYear:int) -> None:
        self.___name = name
        self.__surname = surname
        self.__birthYear = birthYear

    
    @property
    def name(self):
        return self.___name
    

    @property
    def surname(self):
        return self.__surname
    

    @property
    def birthYear(self):
        return self.__birthYear


    @name.setter
    def name(self, new_name):
        self.___name = new_name
    
    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname
    
    @birthYear.setter
    def birthYear(self, new_birthYear):
        self.__birthYear = new_birthYear
    
    def __str__(self) -> str:
        return f"Author: {self.name} {self.surname} , with birthyear: {self.birthYear} \n"
    
def main():
    fredric = Author("Frederic" , "Chopin" , 1849)
    print(fredric)

main()

