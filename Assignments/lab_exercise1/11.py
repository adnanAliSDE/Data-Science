"""
11. Given a student's marks (out of 100), print the grade:
a. 90-100: "A+"
b. 80-89: "A"
c. 70-79: "B"
d. 60-69: "C"
e. 50-59: "D"
f. Below 50: "Fail"
"""
marks = 75
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 50:
    print("D")
else:
    print("Fail")

# Output: B