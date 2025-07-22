''' Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user. '''
oneSubjectTotalMarks=100
mark1=int(input("Enter marks of subject 1: "))
mark2=int(input("Enter marks of subject 2: "))
mark3=int(input("Enter marks of subject 3: "))
totalmarks=oneSubjectTotalMarks*3
obtainedMarks=((mark1+mark2+mark3)/totalmarks)*100

if(obtainedMarks>=40 and (mark1/oneSubjectTotalMarks)*100>=33 and (mark2/oneSubjectTotalMarks)*100>=33 and (mark3/oneSubjectTotalMarks)*100>=33):
    print(f"You are passed with {obtainedMarks}%")
else:
    print(f"You are failed.")