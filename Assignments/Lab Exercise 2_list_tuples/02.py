"""
Problem 2: Tuple Operations
Problem Statement: Write a Python program that:
1. Takes a tuple of numbers as input.
2. Finds the minimum and maximum value in the tuple.
3. Converts the tuple into a list and adds a new element to it.
4. Converts the list back into a tuple and prints the final tuple.
Input Format: A tuple of integers separated by space.
Output Format:
 The minimum and maximum values.
 The modified tuple after adding an element.
Example Input:

(5, 12, 7, 18, 3)
Example Output:
Minimum: 3, Maximum: 18
(5, 12, 7, 18, 3, 25)

"""

t = input("Enter your numbers: ").split(" ")
for i in range(len(t)):
    t[i] = int(t[i])

t = tuple(t)
print(f"Minimum: {min(t)},Maximum: {max(t)}")

t = list(t)
t.append(23)
t = tuple(t)

print(t)
