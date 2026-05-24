
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
"""multi-line
comment"""
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
num1=10
num2=3.14
sum=num1+num2
print(sum)
print(type(sum))
num3=int(num2) #converting float to int
print(num3)
name=input("Enter your name: ")
print("welcome",name)
a=2
b=3
print(a+b)
num1 = int(input("num1:"))
num2 = int(input("num2:"))
print(num1+num2)
side = int(input("side:"))
print("Area of square:", side * side)
num1 = float(input("num1:"))
num2 = float(input("num2:"))
sum = num1 + num2
average = sum / 2
print(average)
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
