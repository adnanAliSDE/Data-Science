"""
7. A year is a leap year if:
a. It is divisible by 400, or
b. It is divisible by 4 but not by 100.
 Write a Python program to check if a given year is a leap year.
"""

year=int(input("Enter the year: "))

if (year%400==0 or year%4==0) and (not year%100==0):
    print("Year is leap")
else:
    print("Not leap year")