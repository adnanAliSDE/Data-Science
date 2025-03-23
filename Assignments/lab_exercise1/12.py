"""
12. Given three sides of a triangle, determine its type:
a. If all three sides are equal, print "Equilateral"
b. If two sides are equal, print "Isosceles"
c. If all three sides are different, print "Scalene"
d. If it does not form a valid triangle, print "Not a Triangle"
Input: 5 5 8
Output: Isosceles

"""

a = 5
b = 5
c = 8
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or c == a:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Not a Triangle")
# Output: Isosceles
