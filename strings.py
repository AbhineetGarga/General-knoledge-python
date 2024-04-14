name = 'harry'
alpha= "ahsvgfdahgfhg&@1233"

print(name)

# slicing method
print(name[0:3])#start from 0 & go all the way till 2 (0 to n-1)
print(name[1:4])#start from 1 & go all the way till 3 (0 to 4-1)

print(name[-3:])
# print(name[-2:])
# print(name[-1:])
print(name[-2:-1])
print(name[-2:-2])


# DIFFERENT METHODS
print(name.upper())
print(name.lower())
print(name.count("r")) #count the number of repetetion
print(alpha.isalnum()) # check if its alpha numeric or not
# print(name.swapcase())
# print(name.title())
# print(name.strip())
# print(name.rstrip())
# print(name.lstrip())
# print(name.rsplit())
# print(name.rsplit('.'))
# print(name.rsplit('.', 1))
# print(name.rsplit('.', 2))