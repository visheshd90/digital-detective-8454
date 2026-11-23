# Number Converter Program
user_input = input("Enter a decimal number: ")
num = int(user_input)

binary_result = bin(num)
hex_result = hex(num)

print(f"Binary output: {binary_result}")
print(f"Hexadecimal output: {hex_result}")
