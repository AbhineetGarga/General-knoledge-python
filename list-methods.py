l1 = [1,2,3,4,5,6,2, 2, 2,7,8,9,10, "Abhineet"]  #First method of list
l2 = [1,2,3,4,5,6,7,8,9,10, "a","b","c","d","e","f","g","h", True, False, ] # we can use any kind of data types inside the list
l3 = [1,2,3,4,5,6,2, 2, 2,7,8,9,10]
print(l1)
print(type(l1)) # to find type of a list
print(l2)

l1.remove("Abhineet")
print(l1)
l3.sort()
print(l1.count(2))
l1.append("Garga") # to add a new entity in your string
l1.extend([11,12,13,14,15,16,17,18,19,20]) # extend your elements is list similer to append function
l3.clear()# clear the whole list
l1.index(2)
print(l3)
print(l1)

#one inportant features in list

l1[0] = "Garga"
print(l1)


'''
There are many methods of list all methods are  not possible to depict here but
i beleve you can google yourself
'''
'''
Note: We can also perform  the slicing operations on a list
'''