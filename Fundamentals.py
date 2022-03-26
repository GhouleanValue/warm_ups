#Data type exercise
#Type out data types and use the print function to see them in the output window 
#We will use the 'type' keyword to show us the data type

#int
print(type(1))

#float
print(type(2.2))

#str
print(type('string'))

#tuple
print(type((1,2,3)))

#set
print(type({1,2,3}))

#dict
print(type({'dict': 'val1', 'dict2': 'val2'}))

#list
print(type([1, 2, 3, 4]))

#bool
print(type(True)) 



#Variable,Operator,and formatting Exercise 

#1 | Assigning variables, multiplying and dividing them

a = 10
b = 20
c = 2

d = (a * b) / c

print(d)

#2 | Mod operator 

a = 2
b = 2
c = a + b

d = c % 2

print(d)

#3 | Concatenation 

x = 'Hello '
y = 'World'
z = x + y

print(z)

#4 | Formating 

x = 10
print('One plus nine is {}'.format('10'))

#5 | Formatting 

print('{0:2} | {1:2} | {2:2}'.format('Code', 'Every', 'Day!'))

#If you did not understand something in this exercise thats great! Take this opportunity to look it up and type it out.
