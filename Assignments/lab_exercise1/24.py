N = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci Series:", end=" ")

for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b
