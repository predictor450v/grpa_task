'''it of Wisdom 📖 In context of general incremental definite loops the structure of while loop can be converted to a for loop using range. Refer this.

# the while loop
i = 0 # initialization
while i<10: # condition
    print(i) # body
    i+=2 # update

# same with for loop
for i in range(0,10,2): # range combines initalization, temination and update.
    print(i)
Write a multi functional program that takes input task from standard input and does the corresponding taks accordingly. Note that the useage of for loop is not allowed in this exercise.

Part 2 - for loop With range
sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
Input - n:int
from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
Input - n:int, k:int
part 3 - for loop with iterables.
string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
Input - s:str
list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
Input - l:list
'''

'''no use of while loop
your code should not use more than 7 for loops 
assuming one for loop per problem
This is the first line of the exercise'''
# Part 1 - while loop to for loop
# factorial - print factorial of a given non-negative integer n (Type: Accumulation)
# Input - n:int
# even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
# Input - n:int
# power_sequence - Print the sequence 1, 2, 4, 8, 16, ... n terms in same line in multiple lines, where n is taken from the input(Type: Mapping)
# Input - n:int
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
task = input(
    "Choose a task:\n"
    "1. factorial\n"
    "2. even_numbers\n"
    "3. power_sequence\n"
    "4. sum_not_divisible\n"
    "5. from_k\n"
    "6. string_iter\n"
    "7. list_iter\n"
    "Enter your choice: "
)

if task == '1':
    n = int(input("enter a non-negative integer for factorial: "))

    if n == 0 or n == 1:
        result = 1
        print(result)
    elif n < 0:
        print("Invalid")
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        print(result)

    
elif task == 'even_numbers':
    n = ...
    while i< n+1:
        print(i)
        i+=2

elif task == 'power_sequence':
    n = ...
    result = 1
    while i<n:
        print(result)
        result*=2
        i+=1

elif task == 'sum_not_divisible':
    ...

elif task == 'from_k':
    ...

elif task == 'string_iter':
    ...

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input

'''if task == 'factorial':
    n = int(input())
    result = 1
    i = 1
    while i <=n:
        result*=i
        i+=1'''
else:
    print("Invalid")