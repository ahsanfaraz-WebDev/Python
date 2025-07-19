# Write a Python program that takes a user's age as input
#  and determines if they are eligible to vote. If the age is 18 or older,
#  print a message using an f-string stating they can vote and how many years
#  they’ve been eligible. If not, use a conditional expression to print how many years
#  are left until they can vote, incorporating a logical operator
#  to check if the input is a valid positive number.

# correct code snippet
# try:
#     age = int(input("Enter your age: "))
#     if age > 0:  # Logical operator to check valid positive number
#         left = f"{18 - age} years left until you can vote" if age < 18 else f"You can vote and have been eligible for {age - 18} years."
#         print(left)
#     else:
#         print("Please enter a positive age.")
# except ValueError:
#     print("Please enter a valid integer age.")


age= int(input("Enter your age: "))

if age>=18:
    print(f"They can vote and {age-18} years They have been eligible.")

left=f"{18-age} years left" if age<18 else f"They can vote and {age-18} years They have been eligible."
print(left)
