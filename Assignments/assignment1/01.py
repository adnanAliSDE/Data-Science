"""
1. Lets start with a simple problem - you need to write a program which does the following
•	Accepts the number of inputs / test cases as 't'
o	The only line of each test case contains 2 integers - declare them as variables A and B
•	For each test case, you need to perform the following operations
o	Create a variable - S - the sum of the 2 input integers
o	Create a variable - P - the product of the 2 input integers
o	Output 2 space separated integers - S and P in a single line
"""

t = int(input("Enter the number of test cases: "))
for i in range(t):
    print("\nTest case", i + 1)
    inputs = input("Enter a,b: ").split(",")

    A, B = int(inputs[0]), int(inputs[1])
    A, B = 1, 2
    S = A + B
    P = A * B
    print(S, P)
