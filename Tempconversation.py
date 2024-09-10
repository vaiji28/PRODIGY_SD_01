def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def temperature_conversion():
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of temperature (Celsius, Fahrenheit, Kelvin): ").strip().lower()

    if unit == "celsius":
        print(f"{temp} Celsius is equivalent to:")
        print(f"{celsius_to_fahrenheit(temp):.2f} Fahrenheit")
        print(f"{celsius_to_kelvin(temp):.2f} Kelvin")
    
    elif unit == "fahrenheit":
        print(f"{temp} Fahrenheit is equivalent to:")
        print(f"{fahrenheit_to_celsius(temp):.2f} Celsius")
        print(f"{fahrenheit_to_kelvin(temp):.2f} Kelvin")
    
    elif unit == "kelvin":
        print(f"{temp} Kelvin is equivalent to:")
        print(f"{kelvin_to_celsius(temp):.2f} Celsius")
        print(f"{kelvin_to_fahrenheit(temp):.2f} Fahrenheit")
    
    else:
        print("Invalid unit. Please enter Celsius, Fahrenheit, or Kelvin.")





