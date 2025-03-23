
"""
Problem 3: Basic List Operations
Problem Statement: Write a Python program that:
1. Takes a list of numbers as input.
2. Finds the largest and smallest numbers in the list.
3. Counts the occurrence of a user-given number in the list.
Input Format: A list of integers separated by space. A single integer to count occurrences.
Output Format:
- The largest and smallest numbers.
- The count of the given number.
Example Input:
10 20 30 40 50 20 10
20
Example Output:
Largest: 50, Smallest: 10
Count of 20: 2
"""

# Taking input from the user
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
target = int(input("Enter the number to count occurrences: "))

# Finding the largest and smallest numbers
largest = max(numbers)
smallest = min(numbers)

# Counting the occurrence of the target number
count = numbers.count(target)

# Printing the results
print(f"Largest: {largest}, Smallest: {smallest}")
print(f"Count of {target}: {count}")
