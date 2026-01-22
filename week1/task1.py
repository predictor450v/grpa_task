'''Tasks 1 to 3 - building up Arithemetic expression
Tasks 4 and 5 - floating point arithemetic
Tasks 6 and 7 - modulo and floor division
Problem Type: Input variable - Output Variable, Hidden suffix for evaluation'''

a=int(input("value of a\n"))
b=int(input("value of b\n"))

output1 = (a + b) # int: sum of a and b
output2 = 2*(a + b) # int: twice the sum of a and b
output3 = abs(a - b)# int: absolute difference between a and b
output4 = abs((output1)-(a*b)) # int: absolute difference between sum and product of a and b
print(f'the sum of a and b {output1}\ntwice the sum of a and b {output2}\nabsolute difference between a and b {output3}\nabsolute difference between sum and product of a and b {output4}')


price, discount_percent = (int(input('price\n')),int(input('discount%')))
# Find discounted price given price and discount_percent
# input variables : price: int, discount_percent: float
discounted_price = float(price*(discount_percent/100)) # float
print(f'discounted price is {discounted_price}')
# Round the discounted_price
rounded_discounted_price = print(f'rounded off {int(discounted_price)}') # int


total_mins = int(input("total mins\n"))
# Find hrs and mins given the total_mins
# input variables : total_mins
hrs = (total_mins//60) # int: hint: think about floor division operator
mins = int(total_mins%60) # int
print("hours",hrs)
print("min",mins)
