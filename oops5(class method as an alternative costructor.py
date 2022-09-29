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

harry = Employee.from_string('Harry-455-Instructor')
harry = Employee('Karan',555,'Student')
print(harry.name,harry.salary,harry.role)
