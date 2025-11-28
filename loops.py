# Loops
# For loops:
# Use them when you know the number of a sequence to iterate over.
# Syntax:
#for val in loop:
   # statment to be executed
# The range function generates s sequence of numbers. It takes one for two arguments.
#example:
for num in range(1,7):
    print(num) 
# Enumerated loops:
# Syntax:
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

# While loops:
count = 1
while count < 10:
    #code is executed as long as the statement is true
    count < 10
    print(count)
    count += 1  # This increments the count by 1 each time the loop runs   

# The loop flow:
# Set the initial point
# set the condition: when the loop should start and stop
# execution: do the task inside the loop
# Update: make changes to the loop variable to eventually meet the exit condition
# Repeat: The loop goes back to another condition is the first one is not true

# We can access the index (i below) of each element in a loop using the enumerate() function.
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i, square in enumerate(squares):
    print(i, square)

# the break statement interrupts the loop when after the condition is met
for num in range(1, 10):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print(num)

# TThe continue statement skips the current iteration and moves to the next one
for num in range(1, 10):
    if num == 5:
        continue
    print(num)
# Here number 5 is skipped in the output (continue acutally mean skip the iteration)

# Quiz 1: Write a for loop that prints out all the elements between -5 and 5 using the range function
for i in range(-5,6):
    print(i)

# Quiz 2: print genres with a loop
Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in Genres:
    print(i)  

# Quiz 3: Using a while loop, print out all the ratings in the PlayListRatings list.

PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
while i < len(PlayListRatings):
    rating = PlayListRatings[i]
    if i < 6:
        break
    print(PlayListRatings)
    i +=1

# Quiz 4: Using a while loop, remove all the 'orange' elements from the squares list and add them to the empty_squares list.

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
empty_squares = []

while squares:                # while the list is not empty
    color = squares.pop(0)    # take the first element
    if color == 'orange':     
        empty_squares.append(color)  # add it to the new list
        
print(empty_squares)

# Quiz 5: Using a for loop and the continue statement, print all the numbers from 0 to 15 except 3 and those greater than 12.
for i in range(0,16):
    if i == 3:
        continue
    elif i > 12:
        continue
    else: print(i)

