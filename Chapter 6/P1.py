nmb1=int(input("Enter the first number: "))
nmb2=int(input("Enter the second number: "))
nmb3=int(input("Enter the third number: "))
nmb4=int(input("Enter the fourth number: "))


if(nmb1>nmb2 and nmb1>nmb3 and nmb1>nmb4):
    print(f"number {nmb1} is the greatest.")
elif(nmb3>nmb2 and nmb3>nmb1 and nmb3>nmb4):
    print(f"number {nmb3} is the greatest.")
elif(nmb2>nmb1 and nmb2>nmb3 and nmb2>nmb4):
    print(f"number {nmb2} is the greatest.")
else:
    print(f"Number {nmb4} is the greatest.")