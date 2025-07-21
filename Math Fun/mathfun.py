import math

print("Available math functions:")
print("1. abs (absolute value)")
print("2. max (maximum of numbers)")
print("3. min (minimum of numbers)")
print("4. pow (power, base^exponent)")
print("5. round (round to n decimal places)")
print("6. sum (sum of numbers)")
print("7. sqrt (square root)")
print("8. math.pow (power, base^exponent)")
print("9. floor (largest integer <= number)")
print("10. ceil (smallest integer >= number)")
print("11. trunc (truncate to integer)")
print("12. fabs (absolute value as float)")
print("13. factorial (factorial of non-negative integer)")
print("14. degrees (radians to degrees)")
print("15. radians (degrees to radians)")
print("16. sin (sine of angle in radians)")
print("17. cos (cosine of angle in radians)")
print("18. tan (tangent of angle in radians)")

try:
    choice = int(input("Enter the number (1-18) of the function to use: "))
    
    # Single-number functions (except factorial, which needs integer)
    if choice in [1, 5, 7, 9, 10, 11, 12, 14, 16, 17, 18]:
        num = float(input("Enter a number: "))
        
        if choice == 1:  # abs
            result = abs(num)
            print(f"Absolute value of {num} is {result}")
        
        elif choice == 5:  # round
            decimals = int(input("Enter number of decimal places to round to: "))
            if decimals >= 0:
                result = round(num, decimals)
                print(f"{num} rounded to {decimals} decimal places is {result}")
            else:
                print("Error: Decimal places must be non-negative")
        
        elif choice == 7:  # sqrt
            if num >= 0:
                result = math.sqrt(num)
                print(f"Square root of {num} is {result}")
            else:
                print("Error: Cannot compute square root of a negative number")
        
        elif choice == 9:  # floor
            result = math.floor(num)
            print(f"Floor of {num} is {result}")
        
        elif choice == 10:  # ceil
            result = math.ceil(num)
            print(f"Ceiling of {num} is {result}")
        
        elif choice == 11:  # trunc
            result = math.trunc(num)
            print(f"Truncated value of {num} is {result}")
        
        elif choice == 12:  # fabs
            result = math.fabs(num)
            print(f"Absolute value (float) of {num} is {result}")
        
        elif choice == 14:  # degrees
            result = math.degrees(num)
            print(f"{num} radians is {result} degrees")
        
        elif choice == 16:  # sin
            result = math.sin(num)
            print(f"Sine of {num} radians is {result}")
        
        elif choice == 17:  # cos
            result = math.cos(num)
            print(f"Cosine of {num} radians is {result}")
        
        elif choice == 18:  # tan
            if math.cos(num) != 0:  # Avoid division by zero
                result = math.tan(num)
                print(f"Tangent of {num} radians is {result}")
            else:
                print("Error: Tangent is undefined at this angle")
    
    # Factorial (requires non-negative integer)
    elif choice == 13:
        num = int(input("Enter a non-negative integer: "))
        if num >= 0:
            result = math.factorial(num)
            print(f"Factorial of {num} is {result}")
        else:
            print("Error: Factorial is not defined for negative numbers")
    
    # Power functions (require base and exponent)
    elif choice in [4, 8]:
        base = float(input("Enter the base: "))
        exp = float(input("Enter the exponent: "))
        if choice == 4:  # pow
            result = pow(base, exp)
            print(f"{base} raised to {exp} is {result}")
        elif choice == 8:  # math.pow
            result = math.pow(base, exp)
            print(f"{base} raised to {exp} is {result}")
    
    # Multi-number functions (max, min, sum)
    elif choice in [2, 3, 6]:
        count = int(input("How many numbers do you want to enter? (2 or more): "))
        if count >= 2:
            numbers = [float(input(f"Enter number {i+1}: ")) for i in range(count)]
            if choice == 2:  # max
                result = max(numbers)
                print(f"Maximum of {numbers} is {result}")
            elif choice == 3:  # min
                result = min(numbers)
                print(f"Minimum of {numbers} is {result}")
            elif choice == 6:  # sum
                result = sum(numbers)
                print(f"Sum of {numbers} is {result}")
        else:
            print("Error: Please enter at least 2 numbers")
    
    else:
        print("Error: Invalid choice. Please select a number between 1 and 18")
        
except ValueError:
    print("Error: Please enter valid numbers")