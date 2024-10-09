unit = input("Is the temperature in Celsius or Farhenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp)/5 + 32, 1)
    print(f"The temperature in Farhenheit is {temp}°F")

elif unit == "F":
    temp = round((temp-32)*5 /9, 1)
    print(f"The temperature in Celcius is {temp}°C")

else:
    print(f"The {unit} of measurement is invalid")
