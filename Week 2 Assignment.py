#Week 2 homework assigmnet

#1 print binary and decimal
#user input
x = int(input("Enter a number: "))

#print value in decimal and binary
print("Decimal:", x)
print("Binary:", bin(x))



#2 error message
#Error occurs because "bin" function only works with integers not all real numbers
#TypeError: 'float' object cannot be interpreted as an integer



#3 assign binary or hex value to variable
y = 0b1011 #binary
z = 0xA3 #hexadeciaml

#print values
print("Binary value (y):", y)
print("Hexadecimal value (z):", z)



#4 add numbers in any representation
#user input x, y, z
x = int(input("Enter a decimal, binary, or hex number for x: "), 0)
y = int(input("Enter a decimal, binary, or hex number for y: "), 0)
z = int(input("Enter a decimal, binary, or hex number for z: "), 0)

#Math
w = x + y + z

# Print result
print("The sum is:", w)



#Compression

#1 choose meaningful variable names
#value to variables # t = text
og_t_size = float(input("Enter the original text size: "))
compressed_t_size = float(input("Enter the compressed text size: "))
dictionary_size = float(input("Enter the dictionary text size: "))

#calculate compression
percent_compression = 1 -((compressed_t_size + dictionary_size) / og_t_size)

#print results
total_size = compressed_t_size + dictionary_size
print(f"Compressed text size:  {compressed_t_size} characters")
print(f"     Dictionary size:  {dictionary_size} characters")
print(f"               Total:  {total_size} characters")
print(f"  Original text size:  {og_t_size} characters")
print(f"         Compression:  {percent_compression:.2%}")
