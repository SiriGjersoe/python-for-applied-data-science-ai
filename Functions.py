# Functions
# Functions encapuslate code for reusability and better organization.
# A function is defined using the def keyword, followed by the function name and parentheses.

from unittest import result


def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b
result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12

def function_name(parameters):
    # Function body
    pass  # Placeholder for function code. Can be a syntactic requirement when no code is needed.

def multiply(a,b):
    #Document what your function does like this:
    """This function multiplies two numbers and returns the product.""" ''
    product = a * b

# The return statement sends the result back to the caller.
# It gives back a value from a function 
# Ends the function execution and sends the result
# If there is no return statement, the function returns None. 


# Scope: Gloal scope: defined outside the function
# Local scope: defined inside the function
# global variables are accessible inside and outside of functions


###########################
# #Functions and loops together

# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)

data_structure = []
element = 5
add_element(data_structure, element)
print(data_structure)

# Function to remove an element from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")

data_structure = [5, 10, 15]
element = 5
# Call the function to remove the element
remove_element(data_structure, element)

print(data_structure)

#get info the function by:
help(len) 


# Instead of having a block like this:
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   

# We can create a function to do the same task:
def calculate (a,b):
    c = a + b + 2 * a * b - 1
    if c < 0:
        c = 0
    else:
        c = 5
    return(c)
calculate(0,0)
print(calculate(0,0))

# In-built functions:
sum(1,2) # gives an error because it takes a tuple or list as argument
a = (1,2)
sum(a) # correct usage

# We can also use loops inside functions:
def loop_calculator(a):
    c = [1,2,3,4,5]
    result = []
    for i in c:
        result.append(i + 2)
    return result

print(loop_calculator(2))

# With strings:
string = "Hello, welcome to the world of Python programming."
def string_checker(text):
    if text in string:
        return True
    else: 
        return False

string_checker("welcome")

#Count the Frequency of Words Appearing in a String Using a Dictionary.
# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")

# Set a default argument value in a function
def default_tip(tip=5):
    if tip >= 4:
        print("very generous")
    else: 
        print("you can do better")
default_tip(4)

# Collections and functions
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

# The argumeents can also be packed into a dictionary
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

#Quiz 1: Come up with a function that divides the first input by the second input:
def divide_function(input1,input2):
    total = input1/input2
    return total

print(divide_function(3,2))

#Can the con function we defined before be used to add two integers or strings?
# Yes
def con(a, b):
    return(a + b)
con(1, 2)

# Quiz 3: Can the <code>con</code> function we defined before be used to concatenate lists or tuples?
# Yes
def con(a, b):
    return(a + b)
con(1, 2)


#Quiz 4: Write a function that counts how many times the word 'little' appears in the string variable string1.
#  solution for Quiz 4:
string1 = ['Mary had a little lamb Little lamb, little lamb Mary had a little lamb. Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go']
def count_little(text,word):
    words = text.lower().split()   # split the text into words
    return words.count(word.lower())  # count the chosen word

print(count_little(string1[0],'little'))

# The official solution for Quiz 4:
def freq(string,passedkey):

    #step1: A list variable is declared and initialized to an empty list.
    words = []

    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()

    #step3: Declare a dictionary
    Dict = {}

    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        if(key == passedkey):
            Dict[key] = words.count(key)   
    #step5: Print the dictionary
    print("Total Count:",Dict)

#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go","little")