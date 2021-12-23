class Student:
    __name:str          #using two underscore because it is a private value
    __surname:str
    __id:str
    __score:float


    #Create Init method for initialization values
    def __init__(self,name:str, surname:str, id:str, score:float) -> None:
        self.__name = name
        self.__surname = surname
        self.__id = id
        self.__score = score
    

    # Create Getters


    #Using decorators to create getters

    # @property
    # def name(self):
    #     return self.__name

    # @property
    # def surname(self):
    #     return self.__surname
    
    # @property
    # def id(self):
    #     return self.__id

    # @property
    # def score(self):
    #     return self.__score


    #Withouth using decorators

    def get_name(self):
        return self.__name
    


    def get_surname(self):
        return self.__surname
    

    def get_id(self):
        return self.__id
    

    def get_score(self):
        return self.__score

    # Create Setters

    #Create Setters with decorator

    # @name.setter
    # def name(self, new_name):
    #     self.__name = new_name
    

    # @surname.setter
    # def surname(self, new_surname):
    #     self.__surname = new_surname
    

    # @id.setter
    # def id(self, new_id):
    #     self.__id = new_id
    
    # @score.setter
    # def score(self, new_score):
    #     self.__score = new_score
    
    #Create setters withouth decorators

    def set_name(self,new_name):
        self.__name = new_name
    
    
    def set_surname(self,new_surname):
        self.__surname = new_surname
    

    def set_id(self,new_id):
        self.__id = new_id
    

    def set_score(self,new_score):
        self.__score = new_score


    #creating string method
    def __str__(self) -> str:
        return f"Student: {self.__name} {self.__surname} with ID:{self.__id} and score {self.__score} "


student = Student("Joe", "Smith", "JS12/20", 8.8)
print(student)

print(student.get_name())
print(student.get_surname())
print(student.get_id())
print(student.get_score())
new_score = 9.4                 
student.set_score(new_score)    #Setting a new student score using set method
print(f"New score {student.get_score()}")   
student.set_id("JSJunior2/19")      
print(student)