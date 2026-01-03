# problem Type: Standard Output - Standard Output
'''
You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.
The operations your application should support are as follows:
'''


'''task 1
Odd number checker: Check whether the input number is odd.
Name: odd_num_check
Inputs: number:int
Output: "yes" if the number is odd, "no" otherwise.'''

def odd_num_check():
    num = int(input("write your number to check odd "))
    if num%2 != 0:
        print("the number is odd ")
    else:
        print("number is even ")
odd_num_check()

'''task 2
Perfect square checker: Check whether the input number is a perfect square.
Name: perfect_square_check
Inputs: number:int
Output: "yes" if the number is a perfect square, "no" otherwise.'''
import math
def perfect_square_check():
    x = int(input("write number to check if it is a perfect square "))
    squa_x = int(math.sqrt(x))
    if squa_x*squa_x == x:
        print("yes the number is perfect squre")
    else:
        print("no the number is not perfect square")
perfect_square_check()


'''task 3
Vowel checker: Check if a string has a vowel in it.
Name: vowel_check
Inputs: text:str
Output: "yes" if the string contains a vowel, "no" otherwise.'''

def vowel_check():
    text = input("write a string to check vowel in it ")
    if set("aeiou") & set(text.lower()):
        print("yes")
    else:
        print("no")
vowel_check()


'''task 4
Divisibility checker: Check if a number is divisible by 2 or 3.
Name: divisibility_check
Inputs: number:int
Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.'''

def divisibility_check():
    number= int(input("write your number "))
    
    if (number%2==0) and (number%3==0):
        print("divisible by both 2 and 3")
    elif (number%2==0):
        print("divisible by 2")
    elif (number%3==0):
        print("divisible by 3")
    else:
        print("non divisible by 2 and 3")
divisibility_check()

'''task 5
Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
Name: palindrominator
Inputs: text:str
Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)'''

def palindrominator():
    text = input("enter the word ")
    new_text = (text + text[-2::-1])
    print(new_text)
palindrominator()

'''task 6
Simple interest calculator with inputs with a higher interest rate if long term.
Name: simple_interest
Inputs: principal_amount:int, n_years:int (number of years)
Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
If the operation name is not any of the above print "Invalid Operation".'''
def simple_interest():
    principal_amount= int(input("enter amount "))
    n_years = int(input("no of years "))
    if (n_years<10):
        r = 5
    else:
        r =8
    si = (principal_amount*r*n_years)/100
    si = round(si)
    print(si)
simple_interest()