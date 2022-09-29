class Employee():
    no_of_leaves = 6  #class variables
    def __init__(self,x,y,z):
        self.name = x
        self.salary = y
        self.role = z
        #what ever work u want to do during the making of objects u can do it in init
        
    def printDetails(self):
        return f"Name is is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newLeaves):
        cls.no_of_leaves = newLeaves
        
harry = Employee('Harry',455,'Instructor')
rohan = Employee('rohan',555,'Student')
harry.change_leaves(33)
print(harry.no_of_leaves)
rohan.change_leaves(55)
print(rohan.no_of_leaves)
