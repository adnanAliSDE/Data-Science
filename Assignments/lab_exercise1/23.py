num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

print(f"Reversed Number: {reversed_num}")

# Check if the number is Armstrong
num = original_num
sum_of_cubes = 0
while num > 0:
    digit = num % 10
    sum_of_cubes += digit ** 3
    num = num // 10

if sum_of_cubes == original_num:
    print(f"{original_num} is an Armstrong number")
else:
    print(f"{original_num} is not an Armstrong number")
