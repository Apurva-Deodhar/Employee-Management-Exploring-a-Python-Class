class Person: 

    def __init__(self, name, weight): 

        self.__name = name 

        self.__weight = weight 

     

    @property 

    def name(self): 

        return self.__name 

  

    @name.setter 

    def name(self, name): 

        self.__name = name 

  

    @property 

    def weight(self): 

        return self.__weight 

  

    @weight.setter 

    def weight(self, weight): 

        self.__weight = weight 

  

class Employee(Person): 

    def __init__(self, name, weight, empid, empsalary): 

        super().__init__(name, weight) 

        self.__empid = empid 

        self.__empsalary = empsalary 

     

    @property 

    def empid(self): 

        return self.__empid 

  

    @empid.setter 

    def empid(self, empid): 

        self.__empid = empid 

  

    @property 

    def empsalary(self): 

        return self.__empsalary 

  

    @empsalary.setter 

    def empsalary(self, empsalary): 

        self.__empsalary = empsalary 

  

  

class Manager(Employee): 

    def __init__(self, name="Ajay", weight=67, empid="CS1002", empsalary=89000, department="Production", no_of_persons=249): 

        super().__init__(name, weight, empid, empsalary) 

        self.__deptmanager = department 

        self.__personsunderhim = no_of_persons 

         

    @property 

    def deptmanager(self): 

        return self.__deptmanager 

  

    @deptmanager.setter 

    def deptmanager(self, department): 

        self.__deptmanager = department 

  

    @property 

    def personsunderhim(self): 

        return self.__personsunderhim 

         

    @personsunderhim.setter 

    def personsunderhim(self, no_of_persons): 

        self.__personsunderhim = no_of_persons 

         

    def display(self): 

        print("Name is", m.name)  

        print("Weight is", m.weight)  

        print("Employee ID is", m.empid)  

        print("Employee Salary is", m.empsalary)  

        print("Department is", m.deptmanager)  

        print("Number of Persons Under Him is", m.personsunderhim)  

  

if __name__ == "__main__": 

    m = Manager() 

    m.name="Apurva" 

    m.weight=67 

    m.empid="CS1009" 

    m.deptmanager="Production" 

    m.personsunderhim=100 

    m.display() 