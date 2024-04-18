dict1= {}
a= {}
print(type(dict1))
print(type(a))


dict1={'good':"something plesent", 'bad':"something else", "1":"The number 1", "2":"The number 2"}
print(dict1)

marks= {"Abhineet":"99", "Shivani": "23", "Ananya": "12", "Akash": "100"} #we can apply a keys of dictionary  seperately and use in a projects
print(marks["Abhineet"])
print(marks["Shivani"])


'''
We can retrive value form keys in dictionary
'''

#add in dictionary

marks["Priyanka"] = 55
print(marks)

# Get Function dont show error when there is no existing key in dictionary
print(marks.get("Priyanka")) # output marks of priyanka
print(marks.get("Priyanka Chopra")) # output none

'''
OR WE CAN ALSO DO IT AS A
print(marks["Priyanka Chopra"]) # it return error 
'''

#To depict all keys present in our dictionery  and values and items
print(marks.keys())

print(marks.values())

print(marks.items())
