"""
10. Write a program to check if a given number is:
a. Divisible by both 3 and 5 → Print "FizzBuzz"
b. Divisible by only 3 → Print "Fizz"
c. Divisible by only 5 → Print "Buzz"
d. Not divisible by either → Print "No FizzBuzz"
Input: 15
Output: FizzBuzz
"""

num = int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0:
    print("Fizz")
elif num%5==0:
    print("Buzz")
else:
    print("No FizzBuzz")