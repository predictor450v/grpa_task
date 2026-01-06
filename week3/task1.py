'''
✅ Important Note on while loop🔁:

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

# odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.
elif task == "odd_char":
    while True:
        line = input()
        if line.endswith("."):
            i = 1
            result = []
            while i <= len(line):
                if i % 2!= 0:
                    result.append(line[i-1])
                i += 1
            print(''.join(result), end=' ')
            break
        i = 1
        result = []
        while i <= len(line):
            if i % 2!= 0:
                result.append(line[i-1])
            i += 1
        print(''.join(result), end=' ')

# Filter and Map - Applying an operation to selected items
# only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. Print the square of each number only if it is even.
elif task == "only_even_squares":
     while True:
        n = input("enter number and to end this \"NAN\"")
        if n.lower() == "nan":
            break
        n = int(n)
        if n % 2 == 0:
            print(n ** 2)


# Filter and Accumulate - Accumulating a result with selected items

# only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.
elif task == "only_odd_lines":
        lines = []
        i = 1
        while True:
            line = input()
            if line == "END":
                break
            if i % 2 != 0:
                lines.append(line)
        i += 1
        print('\n'.join(reversed(lines)))
