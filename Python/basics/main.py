import math
import random #or 'from random import choice'
import statistics
import sys
import json
import re

import cowsay
import requests

import supplementary #importing self made library

def main():

    # Single-line comment
    '''
    multi
    line
    comment
    '''

    a = input("What is your name?  ")

    print("Hello " + a + "!!")
    print("Hello", a, "!!")
    print(f"Hello {a}")

    # Using 'end' and 'sep' in 'print()'
    print("a", end="")  ##end = '\n' by default
    print("a" + "b", sep="")  #sep = " " by default

    # To print quotes within quotes
    print('Hello "friend"')  # Using single quotes
    print("hello \"friend\"")  # Escaping double quotes with backslash

    #strong concatenation using *
    print("meow " * 3)

    # String manipulation
    name = "prapti gupta"
    name1 = "                 PRAPTI                 "
    name2 = "prapti"

    # Removing leading and trailing whitespaces
    print("/" + name1.strip() + "/")  # Removes spaces from both sides
    print("/" + name1.lstrip() + "/")  # Removes spaces from left side
    print("/" + name1.rstrip() + "/")  # Removes spaces from right side
    # Remove specific characters (in this case, 'i')
    print(name2.strip('i'))  # Removes 'i' from both ends

    # Capitalize the first letter
    print(name.capitalize())

    # Convert to title case
    print(name.title())

    # Splitting string into words
    first, last = name.split(" ")  # Splits the name into first and last
    print(first + " | " + last)

    # Basic Calculator
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("Addition:", (x + y))
    print("Subtraction:", (x - y))
    print("Multiplication:", (x * y))
    print("Division:", (x / y))

    #Exponentiation - (a**b)
    #Modulo - (a%b)

    #Rounding
    z = round(x + y)  # Rounding the result to nearest integer
    print(round(z, 2))  # Round to 2 decimal places

    # Adding commas to numbers
    print(f"{z:,}")  # Output 1,000,000 format

    x = pow(2, 2)  # 2 raised to the power of 2
    y = math.sqrt(x)  # Square root of x
    print(x, y)

    # Function
    a = hello("Sweetu")  # Function call with argument
    b = hello()  # Function call without argument (defaults to "world")
    print(a, b)

    #lambda function
    #for inline use/to define a temp function/def function in single line
    sq = lambda x: x ** 2
    print(sq(4))

    # Conditional Statements (if, elif, else)
    if (x < y):
        print(y, "is greater than", x)
    elif (x > y):
        print(x, "is greater than", y)
    else:
        print("Numbers are equal")

    # Logical Operators (`and`, `or`)
    if x > y or x < y:
        print(x, "is not equal to", y)

    if x > 0 and y > 0:
        print("Both are positive numbers")

    # Alternative compact syntax
    #print(True) if n % 2 == 0 else print(False)
    #(if x > 0 and x < 10) = (if 10 > x > 0)

    # Match Statement
    name = input("What's your favourite Harry Potter character?  ")
    
    match name:
        case "Harry" | "Hermione" | "Ron":  # Multiple cases (Harry, Hermione, Ron)
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case "Cedric":
            print("Hufflepuff")
        case "Cho":
            print("Ravenclaw")
        case _:
            print("Who?")  # Default case

    #while loop
    n = 0
    while n != 5:
        print("Meow!")
        n+=1

    #for loop
    for i in range(0,5,1): #range(start,stop,step)
        print("Woof!")

    #list
    #mutable
    students = ["apple","banana","orange"]

    print(students) #print complete list

    print(students[0]) #print each element by index
    print(students[1])
    print(students[2])

    for i in students: #print using for loop
        print(i)

    #len function - works on strings, lists, sets, tuples, dictionaries
    print(len(students))

    #tuple
    #immutable
    students = ("prapti", "aditya")
    print(students[0] + " " + students[1])
    # students[1] = "rudra" will throw error

    #dictionaries
    #immutable
    #exists in key value pairs
    gender = {"Prapti":"F", "Aditya":"M", "Anshika":"F", "Manik":"M"}
    print(gender["Aditya"])

    for i in gender:
        print(i, ": ", gender[i])

    #list of dictionaries
    students = [
        {"name":"Hermione", "house": "Gryffindor", "patronus": "Otter"},
        {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
        {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
        {"name": "Draco", "house": "Slytherin", "patronus": None} #keyword None shows absence of a value
    ]
    #traversing
    for student in students:
        print(f"Name: {student['name']}, House: {student['house']}, Patronus: {student['patronus']}")


    #exception handling
    while True:
        try:
            x = int(input("what's x? "))
        except: #or except ValueError
            print("x is not an integer")
            #or
            #pass
        else:
            break
    print(f"x is {x}")

    #random module
    x = random.choice(["H","T"]) #chooses one
    print(x)
    #or if used 'from' to import
    #x = choice(["H","T"])

    y = random.randint(1,10) #chooses an integer from and including (start,end)
    print(y)

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    random.shuffle(list) #shuffles a list in place
    print(list)

    #stats module
    a = statistics.mean([100,90,80])
    print(a)

    #sys module
    try:
        print("hello, my name is", sys.argv[1]) #argv[0] stores the name of the file
    except:
        #print("enter a name")
        #or
        sys.exit("incorrect input")

    #cowsay package
    #run 'pip install cowsay' in the terminal first
    cowsay.cow("Moo!!")
    cowsay.trex("Rawr!!")

    #API - application programming interface
        #pip install requests
    
    response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
    o = response.json()
    for result in o["results"]:
        print(result["trackName"])

    x= supplementary.goodbye("prapti")
    print(x)

    #regexes
    
    # . - any character except newline
    # * - 0 or more repititions
    # + - 1 or more repititions
    # ? - 0 or 1 repitition
    # {m} - m repitions
    # {m,n} - m-n repititions
    # ^ - matches start of string
    # $ - matches the end of the string just before the newline at the end of the string
    # [] - set of characters
    # [^] - complement of set
    # \w - [a-zA-Z0-9_] (small letters,capital letters,0-9 and _)
    # \W - opp of \w
    # \d - decimal digit
    # \D - not a decimal digit
    # \s - whitespace characters
    # \S - not a whitespace character
    # re.IGNORECASE re.MULTILINE re.DOTALL
    # re.match (no need for ^ at start), re.fullmatch (no need for ^ at start and $ at end)
    # A|B A or B
    # (...) to group


    email = input("What's your email? ").strip()

    if re.search(r"^\w+@(\w+\.)?\w+\.(com|co.in)$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")

    url = input("URL: ").rstrip()
    # username = url.replace("https://twitter.com/","")
    username = re.sub(r"^(https?://)?(www\.)?twitter\.com/" , "" , url)
    print(f"Username: {username}")

#set
#duplicate elements are not allowed
houses = set()
houses.add("Gryffindor")
houses.add("Slytherin")
houses.add("Hufflepuff")
houses.add("Ravenclaw")
houses.add("Gryffindor")
print(houses)

# Function definition
def hello(x="world"):  # Default argument 'world'
    y = ("Hello " + x + " !!")
    return y

# Calling the main function
main()