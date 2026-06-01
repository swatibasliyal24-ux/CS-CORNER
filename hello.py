'''
old = False
a=None
print(type(old))
print(type(a))
#arithmetic operators
a=6
b=3
sum=a+b
print(sum)
print(a-b)
product=a*b
print(product)
quotient=a/b #gives the quotient with the decimal part
print(quotient)
print(a%b)
print(a//b) #gives the quotient without the decimal part
#Hi,I am learning Python programming language.
'''
"""multi-line
comment"""
'''
#relational operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
#assignment operators
a+=6 #a=a+6
print(a)
a-=6 #a=a-6
print(a)
a*=6 #a=a*6
print(a)
a/=6 #a=a/6
print(a)
a%=6 #a=a%6
print(a)
a//=6 #a=a//6
print(a)
'''
'''
#logical operators
x=20
y=30
print(not False)
print(not True)
print(not (x>y))
val1=True
val2=False
val3=True
print(val1 and val2)
print(val1 and val3)
print(val1 or val2)
print(val1 or val3)
#type conversion
'''
'''
num1=10
num2=3.14
sum=num1+num2
print(sum)
print(type(sum))
num3=int(num2) #converting float to int
print(num3)
a=2
b=3
print(a+b)
side = int(input("side:"))
print("Area of square:", side * side)
num1 = float(input("num1:"))
num2 = float(input("num2:"))
sum = num1 + num2
average = sum / 2
print(average)
'''
'''
str="Hello, World!.\nWelcome to Python programming."
print(str)
str1="Hello"
str2="World"
final_str=str1+str2
print(final_str)
length=len(final_str)
print(length)
ch=str[5]
print(ch)
substring=str[0:5]
print(substring)
substring1=str[7:12]
print(substring1)
substring2=str[-5:-1]
print(substring2)
print(str.endswith("programming."))
print(str.replace("World","Python"))
print(str.find("Python"))
first_name=input("First name: ")
length=len(first_name)
print("Length of first name:", length)
str="Hi,$I am the $symbol 99.99"
print(str.count("$"))
'''
'''
age=25
if age>18:
    print("You are an adult.")
elif age==18:
    print("You are just an adult.")
else:
    print("You are a minor.")
num=int(input("Enter a number: "))
if num%2==0:
    print("Even number")
else:
    print("Odd number")
num1=int(input("num1: "))
num2=int(input("num2: "))
num3=int(input("num3: "))
if num1>=num2 and num1>=num3:
    print("Largest number:", num1)
elif num2>=num1 and num2>=num3:
    print("Largest number:", num2)
else:
    print("Largest number:", num3)
marks=[85, 90, 78, 92, 88]
print(marks)
print(type(marks))
print(marks[0])
student=["Alice", 20, "Computer Science", 3.8]
print(student)
'''
'''
list=[1, 2, 3, 4, 5]
list.append(6)
print(list)
list=[2,1,3,5,4]
list.sort()
print(list)
print(list.sort(reverse=True))
print(list)
list.reverse()
print(list)
list.insert(2, 10)
print(list)
list.remove(3)
print(list)
list.pop(4)
print(list)
'''
'''
tup=(1, 2, 3, 4, 5)
print(tup)
print(type(tup))
print(tup[0])
print(tup[1:3])
print(tup.count(3))
print(tup.index(4))
'''
'''
movie1=input("Movie 1: ")
movie2=input("Movie 2: ")
movie3=input("Movie 3: ")
favorite_movies=[movie1, movie2, movie3]
print("Favorite movies:", favorite_movies)
'''
'''
list1=[1, 2, 3]
copy_list=list1.copy()
copy_list.reverse()
if copy_list==list1:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
list=["C","D","A","B","B","A"]
list.count("A")
print(list.count("A"))
list.sort()
print(list)
'''
'''
student_info={
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "GPA": 3.8,
    "favorite_movies": ["Roma", "Titanic", "Avengers"],
    "favorite_colors": {
        "color1": "red",
        "color2": "blue",
        "color3": "green"
    }
}
'''
'''
print(student_info)
print(type(student_info))
print(student_info.items())
print(student_info.values())
print(student_info.keys())
print(student_info.get("name"))
student_info.update({"age": 21})
print(student_info)
'''
'''
collection={1,2,3,4,5}
print(collection)
print(type(collection))
collection.add(6)
print(collection)
collection.remove(3)
print(collection)
collection.clear()
print(collection)
collection={1,2,3,4,5}
collection.pop()
print(collection)
collection1={1,2,3}
collection2={3,4,5}
union_set=collection1.union(collection2)
print(union_set)
intersection_set=collection1.intersection(collection2)
print(intersection_set)
difference_set=collection1.difference(collection2)
print(difference_set)
'''
'''
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts and figures"]
}
print(dictionary)
classroom={"python","java","c++","python","java","javascript","c++","python","c"}
print(len(classroom))
'''
'''
marks = {}

subject_1 = input("Enter subject 1 name: ")
mark_1 = int(input("Enter marks: "))
marks.update({subject_1: mark_1})

subject_2 = input("Enter subject 2 name: ")
mark_2 = int(input("Enter marks: "))
marks.update({subject_2: mark_2})

subject_3 = input("Enter subject 3 name: ")
mark_3 = int(input("Enter marks: "))
marks.update({subject_3: mark_3})

print(marks)
values={9,"9.0"}
print (values)
'''
'''
count=1
while count<=5:
    print(count)
    count+=1
while count>0:
    print(count)
    count-=1
i=1
while i<=100:
    print(i)
    i+=1 
i=100
while i>=1:
    print(i)
    i-=1
n=int(input("Enter a number: "))
i=1
while i<=10:
    print(i*n)
    i+=1
    '''
'''
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
    '''
'''
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter the number to search: "))

i = 0
while i < len(tup):
    if tup[i] == x:
        print("Number found at index", i)
        break
    i += 1
else:
    print("Number not found")
    '''
'''
list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in list:
    print(num)
    '''
'''
tup=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
for num in tup:
    if num == 36:
      print("num is found")
      break

print(num)
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for num in nums:
        print(num)
nums=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x=int(input("Enter the number to search: "))
for num in nums:
    idx = nums.index(num)
    if num == x:
        print("Number found at index", idx)
        break
else:
    print("Number not found")
    '''
'''
seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print(seq[4])
'''
'''
seq=range(1, 101)
for num in seq:
    print(num)
    '''
'''
seq=range(100,0,-1)
for num in seq:
    print(num)
'''
'''
n=int(input("Enter a number: "))
for i in range(1, 11):
    print(i*n)
    '''
'''

n = int(input("Enter a number: "))
i = 1
c = 0

while i in range(1, n + 1):
    c = c + i
    i += 1

print(c)
'''
'''
n = int(input("Enter a number: "))
c=1
i=1
for i in range(1, n + 1):
    c = c * i
    i += 1
print("Factorial of", n, "is", c)
'''
'''
def calc_sum(a,b):
    sum=a+b
    return sum

n=calc_sum(5,10)
print(n)
'''
'''
def print_hello():
    print("hello")

print_hello()
'''
'''
def calc_average(num1,num2,num3):
    sum=num1+num2+num3
    average=sum/3
    return average

print(calc_average(10,20,30))
'''
'''
cities=["New York", "London", "Paris", "Tokyo", "Sydney"]
def print_len(cities):
    print(len(cities))

print_len(cities)    
print(cities[0], end=" ")
print(cities[1], end=" ")
print(cities[2], end=" ")
print(cities[3], end=" ")
print(cities[4], end=" ")
for city in cities:
    print(city, end=" ")
    '''
'''
def factorial(n):
    fact=1
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial of", n, "is", fact)
factorial(5)
'''
'''
def converter(usd_value):
    inr_value=usd_value*82.74
    print("INR value:", inr_value)
converter(1)
'''
'''
#recursion
def show(n):
    if n==0:
        return
    print(n)
    show(n-1)
    print("END")
show(3)
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))   
def sum(n):
    if n==0:
        return 0
    else:
        return n+sum(n-1)
    
print(sum(5))  
def print_list(list, index):
    if index == len(list):
        return
    print(list[index])
    print_list(list, index + 1)
my_list = [1, 2, 3, 4, 5]
print_list(my_list, 0) 
'''   
