"""
6. A shop offers discounts based on the purchase amount:
a. If the amount is above 5000, give a 20% discount.
b. If the amount is between 2000 and 5000, give a 10% discount.
c. Otherwise, no discount.
Write a program to calculate the final price after the discount.
 Input: Purchase Amount: 4500
Output: Final Price: 4050
"""

amt=int(input("Enter the number: "))

dis_perc=0
if amt>5000:
    dis_perc=20
elif amt>2000 and amt<5000:
    dis_perc=10
else:
    dis_perc=0

print("Discount: ",amt*(dis_perc/100))