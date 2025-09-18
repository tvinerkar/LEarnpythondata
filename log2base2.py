#string functions
name = "Ajay"
age = 15
print(name, "is", age, "years old")
print(name +" is "+ str(age) +" years old ")
print(F"{name} is {age} years old")
print("{0} is {1} years old".format(name,age))
print("{n} is {a} years old".format(n=name,a=age))

# input function

# variable = input ('prompt message')

name = input("enter your name")
print(name)

# string typecast issue
a = input("enter 1st number:")
b = input("enter 2nd  number:")
print(a+b)  # will print 111222

# put data type to typecast like int in below example
c = int(input("enter 1st number:"))
d = int(input("enter 2nd  number:"))
print(c+d)

# Arithmetic Operator
a=100
b=10

print("a+b",a+b)  # a+b 110
print("a-b",a-b)  # a-b 90
print("a*b",a*b)  # a*b 1000
print("a/b",a/b)  # a/b 10.0
print("a%b",a%b)  # a%b 0

#Power Operator  **
print(10 ** 2)  # 100
print(5 ** 3) # 125

a = 100
b = 3
print(a**b)    # 1000000

#   Floor Division Operator (return integer value of float)
print(5//2)  # output: 2

#Assignment Operators
a=10
b=5
# Example  output     operator      meaning
a += b #    15          +=          L = L + R

#   Relational Operator  (comapare and return true if match else false)
print (10 == 10)   # True
print (10 != 20)   # True
print (10 <= 20)   # True
print (10 <  20)   # True
print (10 >= 20)   # False
print (10 >  20)   # False

# Logical Operator   (OR, AND , NOT )


