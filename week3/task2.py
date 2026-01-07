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

'''

'''no use of while loop
your code should not use more than 7 for loops 
assuming one for loop per problem
This is the first line of the exercise'''
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
# Part 1 - while loop to for loop
# factorial - print factorial of a given non-negative integer n (Type: Accumulation)
# Input - n:int

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
# even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
# Input - n:int

elif task == '2':
    n = int(input("enter a number to print even numbers till n: "))
    for i in range(0,n):
        if i%2==0:
            print(i)
                                     
# power_sequence - Print the sequence 1, 2, 4, 8, 16, ... n terms in same line in multiple lines, where n is taken from the input(Type: Mapping)
# Input - n:int

elif task == '3':
    n = int(input("enter number of terms in power sequence: "))
      
    for result in range(n):
        
        result = 2**result
        print(result)

# Part 2 - for loop With range
# sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
# Input - n:int

elif task == '4':
    n = int(input("enter a number to find sum of numbers not divisible by 4 and 5: "))
    if n <= 0:
        print("Invalid")
    if n > 0:
        result = 0
        for i in range(n):
            if i % 4 != 0 and i % 5 != 0:
                result += i
        print(result)
    ...

# from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
# Input - n:int, k:int
elif task == '5':
   
   k = int(input("enter starting number k (<=100): "))
   n = int(input("enter number of terms to print n: "))

   count = 0  # Track how many numbers we've found

   for i in range(k, 0, -1):
    # Check if i is odd AND doesn't contain 5 AND doesn't contain 9
        if i % 2 != 0 and '5' not in str(i) and '9' not in str(i):
            # Reverse the digits
            reversed_num = int(str(i)[::-1])
            print(reversed_num)
            
            count += 1
            if count == n:  # Stop after finding n numbers
                break

# part 3 - for loop with iterables.
# string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
# Input - s:str
    
elif task == '6':
    s = input("Enter a string of digits: ")
    prev_digit = 1

    for char in s:
        current_digit = int(char)
        result = current_digit * prev_digit
        print(result)
        prev_digit = current_digit


# list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
# Input - l:list
elif task == '7':
    list = eval(input("provide list []")) # this will load the list from input
    for element in list:
        print(f"{element} - type: {type(element).__name__}")
else:
    print("Invalid")