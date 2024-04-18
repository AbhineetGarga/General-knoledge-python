'''
Created on April 14, 2024

@author: <Abhineet>

it is similer to "switch case statement" in "c" and "c++" language

'''

a=int(input("Enter the number: "))

match a:
    case 1:
        print('Case is one')
    case 2:
        print('Case is two')
    case 3:
        print('Case is three')
    case 33:
        print('Case is Thirty three')
    case 13:
        print('Case is thrirteen')
    case _:
        print("No match found") # default function



#Another example

day = input("The day is: ")

match day:
    case "Monday":
        print("It's Monday!")
    case "Tuesday":
        print("It's Tuesday!")
    case "Wednesday":
        print("It's Wednesday!")
    case _:
        print("It's not Monday, Tuesday, or Wednesday.")