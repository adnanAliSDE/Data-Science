def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


num = int(input("Enter a number: "))
print("Your number is: ", even_odd(num))
