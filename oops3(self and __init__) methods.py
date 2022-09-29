class Employee():
    no_of_leaves = 6  #class variables
    def __init__(self,x,y,z):
        print('x',x)
        print('y',y)
        print('z',z)
        self.name = x
        self.salary = y
        self.role = z
        #what ever work u want to do during the making of objects u can do it in init
        
    def printDetails(self):
        return f"Name is is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee('Harry',455,'Instructor')


'''
harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"


rohan.name = "Rohan"
rohan.salary = 555
rohan.role = "Student"'''


print(harry.salary)

