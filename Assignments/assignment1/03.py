"""
3. You are given a string S consisting of only lowercase English characters.
You need to generate 2 separate strings A and B
•	String A needs to be an exact replica of string S - it has to be created by starting with an empty string
•	String B is reverse of string S.
Input Format
•	The first line will contain t - the number of test cases. Then the test cases follow
•	Each line of the test case consists of a single line of input - the string S
Output Format
•	Each test case will contain 2 lines of output
o	Line 1: Output string A
o	Line 2: Output string B
"""

t = int(input("Enter no. of test cases: "))

for i in range(t):
    print("\nTest Case ", i + 1)
    S = input("Enter a string: ")
    if not S.islower():
        print("Invalid Input")
        continue
    A = "" + S
    B = S[::-1]
    print(A)
    print(B)


