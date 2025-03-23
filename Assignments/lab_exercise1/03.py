def temp_conversion(celcius):
    """
    Converts celcius to fahrenheit
    """
    fahrenheit = (celcius * 9 / 5) + 32
    return fahrenheit


celcius = float(input("Enter celcius temperature: "))
print("Fahrenheit Temperature: ", temp_conversion(celcius))
