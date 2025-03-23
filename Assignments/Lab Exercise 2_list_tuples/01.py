"""
Problem Statement: Write a Python program that takes a list of numbers as input and performs
the following operations:
1. Remove duplicates from the list.
2. Sort the list in ascending order.
3. Reverse the sorted list.
4. Find the second largest number in the list.
5. Find the sum of all elements in the list.
Input Format: A list of integers separated by space.
Output Format:
 The modified list after removing duplicates and sorting.
 The reversed sorted list.
 The second largest number.
 The sum of the list elements.
Example Input:
10 20 20 30 40 10 50
Example Output:
[10, 20, 30, 40, 50]
[50, 40, 30, 20, 10]
40
150
"""

num_inputs = input("Enter your numbers: ").split(" ")

# Typecasting to numbers
for i in range(len(num_inputs)):
    num_inputs[i] = int(num_inputs[i])

# 1. Removing duplicates
nums = []
for num in num_inputs:
    if num not in nums:
        nums.append(num)

nums = sorted(nums)
print(nums)  # sorted in asc order

print(list(reversed(nums)))  # Reverse sorted list

# Finding second largest number
second_num = nums.copy()

second_num.pop(max(second_num))
second_max = max(second_num)

print(second_max)
print(sum(nums))