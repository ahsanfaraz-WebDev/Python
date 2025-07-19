# Create a Python program that prompts the user to enter two numbers
#  and a mathematical operation (addition, subtraction, multiplication, or division).
#  Using the math module for square root and power operations,
#  perform the requested operation if valid; otherwise,
#  use if-else statements with arithmetic and logical operators 
# to print an error message if the operation is invalid or if division by zero is attempted.
import math
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

op=input("Enter one operation from the followings +,-,*,/: ")

if op=="+":
    res=num1+num2
    print(f"Addition of two numbers is {res}")
elif op=="-":
    res=num1-num2
    print(f"Substraction of two numbers is {res}")
elif op=="*":
    res=num1*num2
    print(f"Multiplication of two numbers is {res}")
elif op=="/" and num2!=0:
    res=num1/num2
    print(f"Division of two numbers is {res}")
else:
    print("division by zero not possible")

# sqrt operation on result
aftrSR=round(math.sqrt(res))
print(f"And square root of this operation is {aftrSR}")

# power 4 of result 
aftrPow=round(math.pow(aftrSR,4))
print(f"And taking power 4 after square root of this operation is {aftrPow}")

      
    