class Employee():
    def __init__(self,x,y,z):
        self.name = x
        self.salary = y
        self.role = z
    def printDetails(self):
        return f"The Name is {self.name}"
    @classmethod
    def from_string(cls,string):
        params = string.split('-')
        print(params)
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood(string):
        return f'this is good {string}'

class Programmer(Employee):
    def __init__(self,aname,asalary,arole,alanguage):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage
    def printprog(self):
        return f"Programmers name is {self.name} and salary is {self.salary} and role is {self.role}  and my langauge is {self.language}"



harry = Employee('Harry',455,'Instructor')
rohan = Employee('Rohan',600,'Student')

karan = Programmer('Karan',655,"Programmer",['python'])
shubham = Programmer('Shubham',500,'Programmer',['javascript'])

print(karan.printprog())