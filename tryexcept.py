# it is type of hendling the errors

try:
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    print(a+b)
except:
    print("some error occured")


    #  it is bassically a mwthod of error hendling

#one more way if we want to see the error

try:
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    print(a+b)
except Exception as e:
    print("some error occured", e)
