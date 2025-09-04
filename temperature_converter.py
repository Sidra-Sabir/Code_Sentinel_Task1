
temp = input("Enter temperature: ")
print(f"Temperature is, {temp}")

# everything except last character → number
value = float(temp[:-1])

# last character → C or F (convert to uppercase)   
unit = temp[-1].upper()

if unit == "C":
    # it will Convert Celsius to Fahrenheit
    result = (value * 9/5) + 32
    print(f"{value}C is equal to {result:.2f}F")

elif unit == "F":
    # then it will Convert Fahrenheit to Celsius
    result = (value - 32) * 5/9
    print(f"{value}F is equal to {result:.2f}C")

else:
    print("please! Enter valid temperature 37C or 98F")

