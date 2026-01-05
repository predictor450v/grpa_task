'''
✅ Important Note on while loop🔁:

Use while only when the number of iterations is indefinite.
If you can term the steps as do n times, do once for each item, etc. use for loop instead.
If you can only term the steps as do until something happens. Like when user inputs 10.
A bit of wisdom 📖 There are maily two ways in which while loops are used in the context of taking inputs until a terminal word.

# method 1
a = input()
while a != terminal_word: # opposite of the terminal condition
    # do something with a
    a = input() # take the next a

# method 2
while True: # loop forever
    a = input()
    if a == terminal_word: # the terminal condition
        break
    # do something with a
'''

'''
Problem Statement

Problem type - Standard Input - Standard Output

NOTE: None of this problem statements can be written using a for since the number of repetition is indefinite.

Implement different parts of a multi-functional program based on an initial input value. Each part of the program will handle various tasks related to accumulation, filtering, mapping, and combinations of these operations. None of the tasks should use explicit loops for definite repetitions, and the program should handle indefinite inputs gracefully.

Tasks


odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.
Filter and Map - Applying an operation to selected items
only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. Print the square of each number only if it is even.
Filter and Accumulate - Accumulating a result with selected items
only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.


'''

# This is the first line of the exercise
print("tell which task you want to perform")
task = input("sum_until_0,total_price,only_ed_or_ing,reverse_sum_palindrome,double_string,odd_char,only_even_squares,only_odd_lines ")

# Accumulation - Accumulating a final result
# sum_until_0: Continuously read integers from standard input until you receive a zero. Print the sum of these integers.
if task == "sum_until_0":
    total = 0
    n = int(input())
    while  n != 0: # the terminal condition
        total = total + n # add n to the total
        n= int(input()) # take the next n form the input
    print(total)

# total_price: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string "END". Print the total price of all items.

elif task == "total_price":
    total_price = 0
    while True: # repeat forever since we are breaking inside
        line = input("format:3 500,END :")   # 3 500
        if "END" in line: # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = int(quantity),int(price) # convert to ints
        total_price += quantity*price # accumulate the total price
    print(total_price)

# Filtering - Selecting based on a criterion
# only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output). Print only those strings that end with "ed" or "ing" (case insensitive).

elif task == "only_ed_or_ing":
    while True:
        n = input("enter your string :")
        if "STOP" in n:
            break
        if n.endswith("ed") or n.endswith("ing"):
            print(n)

# reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). Print only those integers for which the sum of the number and its reverse is a palindrome.

elif task == "reverse_sum_palindrome":
    while True:
        a = (input("type numbers"))
        if int(a) == -1:
            break
        reverse_a = a[::-1]
        sum = int(a) + int(reverse_a)
        if str(sum) == str(sum)[::-1]:
            print(f"{sum} is a palimdrome and the input is {a}")

# Mapping - Applying the same operation to different items
# double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.


elif task == "double_string":
    while True:
        line = input("enter your sentence")
        if line =="":
            break
        print(line+line)

elif task == "odd_char":
    ...

elif task == "only_even_squares":
    ...

# elif task == "only_odd_lines":