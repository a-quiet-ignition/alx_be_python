# A simple multiplication table generator

# Prompting user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generating and displaying the multiplication table
for x in range(1, 11):
    product = number * x
    print(number, "*", x, "=", product)