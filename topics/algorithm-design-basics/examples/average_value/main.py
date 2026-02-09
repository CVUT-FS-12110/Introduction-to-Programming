# number of values (constant)
N = 5

total = 0

print(f"Enter {N} numbers:")

for i in range(1, N + 1):
    x = float(input(f"Value #{i}: "))
    total = total + x

average = total / N
print("Average value:", average)
