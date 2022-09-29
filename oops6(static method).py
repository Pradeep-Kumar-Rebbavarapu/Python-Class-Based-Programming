class Employee():
    def __init__(self,x,y,z):
        self.name = x
        self.salary = y
        self.role = z
    @classmethod
    def from_string(cls,string):
        params = string.split('-')
        print(params)
        return cls(params[0],params[1],params[2])

    @staticmethod
    def printgood(string):
        return f'this is good {string}'

harry = Employee.from_string('Harry-455-Instructor')
print(harry.printgood('harry'))
print(Employee.printgood('Employee'))