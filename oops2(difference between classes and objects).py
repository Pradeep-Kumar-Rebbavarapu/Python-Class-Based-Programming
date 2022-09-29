class Employee():
    no_of_leaves = 6  #class variables
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"



rohan.name = "Rohan"
rohan.salary = 555
rohan.role = "Student"

print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)
print('1st dict',harry.__dict__)
harry.no_of_leaves = 16
print('2nd dict',harry.__dict__)
print('dict of rohan',rohan.__dict__)
Employee.no_of_leaves = 9
