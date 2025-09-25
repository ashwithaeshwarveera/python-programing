num1 = int(input("enter first integer:"))
num2 = int(input("enter second integer"))


# bitwise AND
bitwise_and = num1 & num2

# bitwise_OR
bitwise_or = num1 | num2

# bitwise_XOR
bitwise_xor = num1 ^ num2

# bitwise_NOT
bitwise_not_num1 = ~num1
bitwise_not_num2 = ~num2

# bitwise left shift
left_shift = num1 << 1

# bitwise right shift
right_shift = num2 >> 2


print(f"\n bitwise AND of {num1} &{num2}={bitwise_and}")
print(f"\n biwise OR of {num1}|{num2}={bitwise_OR}")
print(f"\n bitwise XOR of {num1}^{num2}={bitwise_XOR}")
print(f"\n bitwise NOT of {num1}={bitwise_not_num1}")
print(f"\n bitwise NOT of {num2}={bitwise_not_num2}")
print(f"\n bitwise left shift of {num1}<<1={left_shift}")
print(f"\n bitwise right shift of {num2}>>2={right_shift}")
