
n = 5
max_value = 0
min_value = 0
count = 0


for i in (range(0, n)):
    x = float(input(f"Value #{i}: "))
    count += 1
    if x > max_value:
        max_value = x
        count = count
    if x < min_value:
        min_value = x

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

