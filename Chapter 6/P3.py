s1="Make a lot of money"
s2="Buy Now"
s3="Subscribe this"
s4="click this"


comment=input("Enter the comment: ")


if(s1 in comment or s2 in comment or s3 in comment or s4 in comment ):
    print("This comment is spam.")
else:
    print("Not a spam comment.")