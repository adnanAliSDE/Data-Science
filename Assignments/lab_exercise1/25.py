"""
25. Write a program to check if a number is an Armstrong number (sum of cubes of its 
digits equals the number).
Input: 153
Output: Armstrong Number
"""
def is_armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        return True
    else:
        return False
    
num = int(input("Enter a number: "))
if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Output: Enter a number: 153
# Armstrong Number
