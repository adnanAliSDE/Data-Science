"""
2. You are given 2 integers: A and C.
You need to find if there exists any integer B which meets the following condition
•	B must be an integer
•	B is the average of A and C.
For each test case, output B. If no such integer exists, output −1.

"""

t = int(input("Enter no. of test cases: "))

for i in range(t):
    inputs = input("Enter A,C: ").split(",")
    A, C = int(inputs[0]), int(inputs[1])
    B = -1
    for j in range(min(A, C), max(A, C) + 1):
        if j == (A + C) / 2:
            B = j
            break
    print(B)
