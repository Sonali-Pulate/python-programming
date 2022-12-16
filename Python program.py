#!/usr/bin/env python
# coding: utf-8

# In[43]:


#Program prints Hello, world!
print('Hello, world!')


# In[44]:


#Program adds two numbers
num1 = 15
num2 = 63
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[45]:


# Add Two Numbers With User Input
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))


# In[46]:


#Program to Check if a Number is Positive, Negative or 0(Using if...elif...else)
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# In[47]:


#Using Nested if
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# In[48]:


#Program to Check if a Number is Odd or Even
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))


# In[7]:


#Program to Check Prime Number Using a flag variable
num = 29
# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")


# In[13]:


#Program to Find the Factorial of a Number using Loop

# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)


# In[1]:


# Program to Find the Factors of a Number
def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)

num = 320

print_factors(num)


# In[3]:


#Program to Find the Square Root
num = 8 
#num = float(input('Enter a number: '))

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))  


# In[5]:


#square root of real or complex numbers
import cmath

num = 1+2j

# To take input from the user
#num = eval(input('Enter a number: '))

num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))


# In[6]:


#Program to Calculate the Area of a Triangle
a = 5
b = 6
c = 7
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# In[8]:


#Program to Solve Quadratic Equation
# Solve the quadratic equation ax**2 + bx + c = 0
import cmath

a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))


# In[9]:


#Program to Swap Two Variables Using a temporary variable
x = 5
y = 10
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# In[10]:


#Without Using Temporary Variable
x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)


# In[11]:


#Program to Generate a Random Number
import random

print(random.randint(0,9))


# In[12]:


#Program to Convert Kilometers to Miles
# Taking kilometers input from the user
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))


# In[14]:


#Program to Convert Celsius To Fahrenheit
celsius = 18

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))


# In[17]:


#Program to Check Leap Year
year =1990
# To get year (integer input) from the user
# year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print("{0} is not a leap year".format(year))


# In[19]:


#Program to Find the Largest Among Three Numbers
num1 = 20
num2 = 24
num3 = 18
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3

print("The largest number is", largest)


# In[21]:


#Program to Display the multiplication Table
num = 15
for i in range(1, 14):
    print(num, 'x', i, '=', num*i)


# In[32]:


#Program to Check Armstrong Number
# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit **3
    temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
else:
        print(num,"is not an Armstrong number")


# In[39]:


#Program to Find the Sum of Natural Numbers
num = 16

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
# use while loop to iterate until zero
while(num > 0):
        sum += num
        num -= 1
        print("The sum is", sum)


# In[40]:


#Program to Display Powers of 2 Using Anonymous Function
# Display the powers of 2 using anonymous function

terms = 10

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
    print("2 raised to power",i,"is",result[i])


# In[42]:


#Program to Find Numbers Divisible by Another Number
my_list = [12, 65, 54, 39, 102, 339, 221,]
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)


# In[43]:


#Program to Convert Decimal to Binary, Octal and Hexadecimal
#Python program to convert decimal into other number systems
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")


# In[44]:


#Program to Find ASCII Value of Character
c = 'p'
print("The ASCII value of '" + c + "' is", ord(c))


# In[66]:


#Program to find the L.C.M. of two input number
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))


# In[1]:


# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])


# In[1]:


#Program to Display Calendar
import calendar

yy = 2014  # year
mm = 11    # month

# To take month and year input from the user
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))


# In[2]:


#Program to Find Sum of Natural Numbers Using Recursion
def recur_sum(n):
   if n <= 1:
       return n
   else:
       return n + recur_sum(n-1)

# change this value for a different result
num = 16

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is",recur_sum(num))


# In[3]:


#Program to Find Factorial of Number Using Recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)

num = 7

# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))


# In[4]:


#Program to Convert Decimal to Binary Using Recursion
def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2,end = '')

# decimal number
dec = 34

convertToBinary(dec)
print()


# In[5]:


#Program to Add Two Matrices
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)

   


# In[6]:


#Program to Transpose a Matrix
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
        result[j][i] = X[i][j]

for r in result:
    print(r)


# In[7]:


#Program to Multiply Two Matrices
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
    print(r)


# In[8]:


#Program to Check Whether a String is Palindrome or Not
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# In[9]:


#Program to Remove Punctuations From a String
# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "Hello!!!, he said ---and went."

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)


# In[10]:


#Program to Sort Words in Alphabetic Order
# Program to sort alphabetically the words form a string provided by the user

my_str = "Hello this Is an Example With cased letters"

# To take input from the user
#my_str = input("Enter a string: ")

# breakdown the string into a list of words
words = [word.lower() for word in my_str.split()]

# sort the list
words.sort()

# display the sorted words

print("The sorted words are:")
for word in words:
    print(word)


# In[11]:


#Program to Illustrate Different Set Operations
# Program to perform different set operations like in mathematics

# define three sets
E = {0, 2, 4, 6, 8};
N = {1, 2, 3, 4, 5};

# set union
print("Union of E and N is",E | N)

# set intersection
print("Intersection of E and N is",E & N)

# set difference
print("Difference of E and N is",E - N)

# set symmetric difference
print("Symmetric difference of E and N is",E ^ N)


# In[12]:


#Program to Count the Number of Each Vowel
# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1

print(count)


# In[17]:


#Program to Create Pyramid Patterns
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")


# In[19]:


#Program to Merge Two Dictionaries
#Using the | Operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print(dict_1 | dict_2)


# In[20]:


#Using the ** Operator
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

print({**dict_1, **dict_2})


# In[21]:


#Using copy() and update()
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}

dict_3 = dict_2.copy()
dict_3.update(dict_1)

print(dict_3)


# In[22]:


#Program to Access Index of a List Using for Loop
#Using enumerate
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)


# In[24]:


#Start the indexing with non zero value
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
    print(index, val)


# In[25]:


#Without using enumerate()
my_list = [21, 44, 35, 11]
for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)


# In[26]:


#Program to Access Index of a List Using for Loop
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list):
    print(index, val)


# In[27]:


#Start the indexing with non zero value
my_list = [21, 44, 35, 11]

for index, val in enumerate(my_list, start=1):
    print(index, val)


# In[28]:


#Without using enumerate()
my_list = [21, 44, 35, 11]
for index in range(len(my_list)):
    value = my_list[index]
    print(index, value)


# In[29]:


#Program to Flatten a Nested List
my_list = [[1], [2, 3], [4, 5, 6, 7]]
flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)


# In[30]:


#Using Nested for Loops 
my_list = [[1], [2, 3], [4, 5, 6, 7]]
flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)
print(flat_list)


# In[31]:


#Program to Slice Lists
my_list = [1, 2, 3, 4, 5]
print(my_list[:])


# In[32]:


#Items at Specified Intervals
my_list = [1, 2, 3, 4, 5]
print(my_list[::2])


# In[33]:


#Program to Check If a List is Empty
#Using Boolean operation
my_list = []
if not my_list:
    print("the list is empty")


# In[34]:


#Using len()
my_list = []
if not len(my_list):
    print("the list is empty")


# In[35]:


#Comparing with []
my_list = []
if my_list == []:
    print("The list is empty")


# In[36]:


#Program to Get the Last Element of the List
#Using negative indexing
my_list = ['a', 'b', 'c', 'd', 'e']

# print the last element
print(my_list[-1])


# In[37]:


#Program to calculate length of a String without using len() function
str = input("Enter a string: ")
# counter variable to count the character in a string
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)


# In[38]:


#Program to find the length of string using library function
# User inputs the string and it gets stored in variable str
str = input("Enter a string: ")
# using len() function to find length of str
print("Length of the input string is:", len(str))


# In[39]:


#Finding largest number in a list using sort() method
# A list of numbers is given
lis = [1, 10, 40, 36, 16]
# sorting the given list "lis"
# sort() function sorts the list in ascending order
lis.sort()
# Displaying the last element of the list
# which is the largest number in the sorted list
print("Largest number in the list is:", lis[-1])


# In[40]:


#Finding largest number in a list using max() method
# Python program to find largest number in a list
# using max() function
# A list of numbers
lis = [19, 10, 45, 26, 6]
# max() method returns the largest element of the list
print("Largest number of the list is:", max(lis))


# In[41]:


#Program to Find largest number in a list
# creating empty list
lis = []
# user enters the number of elements to put in list
count = int(input('How many numbers? '))
# iterating till count to append all input elements in list
for n in range(count):
    number = int(input('Enter number: '))
    lis.append(number)
# displaying largest element
print("Largest element of the list is :", max(lis))


# In[49]:


#set-
#Union
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print ( A | B)


# In[50]:


#Intersection:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print ( A & B )


# In[51]:


#Difference:
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)


# In[55]:


#Arithmetic Operators in python-
a = 21
b = 10
c = 0
c = a + b
print ( c )
c = a - b
print ( c )
c = a * b
print ( c )
c = a / b
print ( c )
b = 3
c = a**b
print ( c )


# In[62]:


#Assignment Operators:
a = 21
b = 10
c = 0
c = a + b
print ( c )
c += a
print ( c )
c *= a
print ( c )
c /= a
print ( c )
c  = 2
c %= a
print ( c )
c **= a
print ( c )


# In[63]:


#Bitwise Operators:
a = 58        # 111010
b = 13        # 1101
c = 0
c = a & b
print ( c )   # 8 = 1000
c = a | b
print ( c )   # 63 = 111111
c = a ^ b
print ( c )   # 55 = 110111
c = a << 2
print ( c )   # 232 = 11101000
c = a >> 2
print ( c )   # 14 = 1110


# In[64]:


#Membership Operators:
X = [1, 2, 3, 4]
A = 3
print(A in X)
print(A not in X)


# In[2]:


#Identity Operators:
X1 = 'Welcome To India!'
X2 = 1234 
Y1 = 'Welcome To India!'
Y2 = 1234
print(X1 is Y1)
print(X1 is not Y1)
print(X1 is not Y2)
print(X1 is X2)


# In[3]:


#Program to Print Output Without a Newline
# print each statement on a new line
print("Python")
print("is easy to learn.")
# new line
print()
# print both the statements on a single line
print("Python", end=" ")
print("is easy to learn.")


# In[4]:


#Program to Count the Occurrence of an Item in a List
#Using count() method
freq = ['a', 1, 'a', 4, 3, 2, 'a'].count('a')
print(freq)


# In[5]:


#Program to Reverse a Number
#using a while loop
num = 1234
reversed_num = 0

while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))


# In[6]:


#Program to Capitalize the First Character of a String
my_string = "programiz is Lit"

print(my_string[0].upper() + my_string[1:])


# In[7]:


#Using inbuilt method capitalize()
my_string = "programiz is Lit"

cap_string = my_string.capitalize()

print(cap_string)


# In[8]:


#Program to Remove Duplicate Element From a List
#Using set()
list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))


# In[9]:


#Remove the items that are duplicated in two lists
list_1 = [1, 2, 1, 4, 6]
list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))


# In[10]:


#Program to Compute the Power of a Number
#using a while loop
base = 3
exponent = 4

result = 1

while exponent != 0:
    result *= base
    exponent-=1

print("Answer = " + str(result))


# In[11]:


#using a for loop
base = 3
exponent = 4

result = 1

for exponent in range(exponent, 0, -1):
    result *= base

print("Answer = " + str(result))


# In[ ]:




