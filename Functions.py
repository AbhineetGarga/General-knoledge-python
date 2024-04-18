def greetHello():                # use def to define function
    print("Hello World!")

print("Exicuting Function...")
greetHello()
print("Exited Function...")




def greetGoodbye(name, ending):    # we pass two variables in our functions and we can use those as a argument
    print("Goodbye " + name)
    print(ending)


greetGoodbye("Abhineet", "tnahkyou") # we can use function multiple time
greetGoodbye("Shivam", "tnahkyou!")



#New concept

#Letter generator

def letter(name, date):
    st=f"Hi maa'm \n \t this is  {name} and i will not  come to school on {date}"
    print(st)


letter("Abhineet", "26th october 2021")



#create a function to find average

def average(a,b):
    return (a+b)/2

print(average(2,4))
print(average(100,50))



'''
it is  not mendetory that We need to  create all the functions There is some builtin functions provided by python itself  for e.g  "print" function and some function we can use as a part of module install by pip
'''
