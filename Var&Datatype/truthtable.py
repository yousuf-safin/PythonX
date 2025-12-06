# values = [True,False]
# print("A\tB\tA or B\tA and B\tNot A")

# print("-"*40)

# for A in values:
#     for B in values:
#         print(f"{A}\t{B}\t{A or B}\t{A and B}\t{not A}")

# Ask user for number of bits (columns)
n = int(input("Enter how many bits/columns you want: "))

# Total rows = 2^n
rows = 2 ** n

print("\nTruth Table:")
print("-" * (n * 8))

# Print header
for i in range(n):
    print(f"A{i+1}", end="\t")
print()

print("-" * (n * 8))

# Print binary truth table
for i in range(rows):
    binary = format(i, f"0{n}b")   # convert to binary with leading zeros
    for bit in binary:
        print(bit, end="\t")
    print()
