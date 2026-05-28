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