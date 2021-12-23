class Person:
    #Create class Person with private attributes name,surname,umnc,height, weight
    __name:str
    __surname:str
    __umnc:int
    __height:float
    __weight:float


    #Init method for initializating all attributes
    def __init__(self, name:str, surname:str, umnc:int, height:float, weight:float) -> None:
        self.__name = name
        self.__surname = surname
        self.__umnc = umnc
        self.__height = height
        self.__weight = weight


    #Getters
    @property
    def name(self):
        return self.__name
    

    @property
    def surname(self):
        return self.__surname
    

    @property
    def umnc(self):
        return self.__umnc

    @property
    def height(self):
        return self.__height
    
    
    @property
    def weight(self):
        return self.__weight
    

    #Setter
    @name.setter
    def name(self, new_name):
        self.__name = new_name
    

    @surname.setter
    def surname(self, new_surname):
        self.__surname = new_surname
    

    @umnc.setter
    def umnc(self, new_umnc):
        self.__umnc = new_umnc
    

    @height.setter
    def height(self, new_height):
        self.__height = new_height

    
    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight
    

    #Function for count BMI
    def count_BMI(self):
        meters = self.__height / 100
        return self.__weight / meters ** 2

    
    #Str method
    def __str__(self) -> str:
        person = f"Name: {self.name} \n"
        person += f"Surname: {self.surname} \n"
        person += f"Umnc: {self.umnc} \n"
        person += f"Height: {self.height} \n"
        person += f"Weight: {self.weight} \n"
        person += f"He's BMI: {self.count_BMI()} \n"
        return person



number_of_person = int(input("How many person do you want to add? "))
list_of_persons = []        #Create empty list of person so we can create list of all person's we added
for i in range(number_of_person):
    name = input("Name: ")
    surname = input("Surname: ")
    umnc = int(input("UMNC: "))
    height = float(input("Height: "))
    weight = float(input("Weight: "))
    print()
    current_person = Person(name,surname,umnc,height,weight)    #Create object from user input
    list_of_persons.append(current_person)                      #Adding objects to list of person

for each_person in list_of_persons:                         #Loop in list of person
    print(each_person)                                      #Print each person


current_lowest_BMI = list_of_persons[0].count_BMI()     #Take BMI from first person in list of person's
current_person_with_lowest_BMI = list_of_persons[0]     #Take first object of class Person
    
for pers in list_of_persons:
    current_BMI = pers.count_BMI()                  #Take current bmi from list of person
    if current_BMI < current_lowest_BMI:            #check if the current bmi is lower than bmi from first person in list 
        current_lowest_BMI  = current_BMI           #IF true change first person with person that has lowest bmi
        current_person_with_lowest_BMI = pers       #Also change the object to person with lowest bmi
    
print(f"Person with lowest BMI: {current_person_with_lowest_BMI}")

total = 0
for pers in list_of_persons:
    person_BMI = pers.count_BMI()           #Take BMI from all person's one by one
    total += person_BMI                     #Every time add he's BMI to sum of 

average_BMI = total / number_of_person      #To generate average BMI we must take total sum of BMI's and devided it with number of person we added 

print(f"Average BMI of all person's in list: {average_BMI} ")

