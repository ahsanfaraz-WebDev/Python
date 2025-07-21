nmb=int(input("Enter the 1st number: "))
nmb2=int(input("Enter the 2nd number: "))
nmb3=int(input("Enter the 3rd number: "))
nmb4=int(input("Enter the 4th number: "))


if(nmb>nmb2 and nmb>nmb3 and nmb>nmb4):
    print("Number 1 is greater.")
elif(nmb2>nmb and nmb2>nmb3 and nmb2>nmb4):
    print("Number 2 is greater.")
elif(nmb3>nmb and nmb3>nmb2 and nmb3>nmb4):
    print("Number 3 is greater.")
else:
    print("Number 4 is greater.")


