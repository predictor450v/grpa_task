# Problem type: Standard Input Standard Output - Input from prefix and Output from suffix


# swap the values of `x1` and `x2`

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 

# create a new variable `a` with the value of `z`

# delete the variable `z`


x1 = input("x1 ")
x2 = input("x2 ")

# to swap we need a temp veriable
temp = x1
x1 = x2
x2 = temp
print(x1)
print(x2)
y1 = input("y1 ")
y2 = input("y2 ")
y3 = input("y3 ")

t1=y1
t2=y2
t3=y3

y1 = t3
y2 = t1
y3 = t2 
print(y1)
print(y2)
print(y3)



z = input("z ")
a = z
del z
print("a =",a)



""" we can do this with 1 variable also with tupple unpacking 

temp = y1
y1 = y2
y2 = y3
y3 = temp


# Two-way swap
x1, x2 = x2, x1

# Circular swap
y1, y2, y3 = y2, y3, y1



"""