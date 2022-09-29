#def function1():
#    print('Subscribe now')

#func2 = function1
#del function1
#func2()

'''def funcret(num):
    if num==0:
        return print
    if num==1:
        return sum

a = funcret(1)
print(a)

def executer(func):
    func('this')

executer(print)'''

def deck1(func1):
    def nowexe():
        print('executing now')
        func1()
        print('Executed')
    return nowexe
@deck1
def who_is_harry():
    print('harry is a good boy')


#who_is_harry = deck1(who_is_harry)
who_is_harry()
