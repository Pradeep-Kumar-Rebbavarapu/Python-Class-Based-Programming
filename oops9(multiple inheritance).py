
class Employee:
    var = 8
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

harry = Employee('Harry',455,'Instructor')
rohan = Employee('Rohan',600,'Student')

class Player:
    var = 9
    no_of_games = 4
    def __init__(self,game,name):
        self.name = name
        self.game = game
    def printDetails(self):
        return f"The Name is {self.name} the game playing is {self.game}"

shubham = Player('Shubham',['cricket','football'])


class CoolProgrammer(Employee,Player): #the order of specifying classes inside brancket is important bcuz 1st class __init__ will be used for defining objects 
   
    language = "c++"
    def printlanguage(self):
        return self.language

karan = CoolProgrammer('Karan',455,'CoolProgrammer')


print(karan.var)