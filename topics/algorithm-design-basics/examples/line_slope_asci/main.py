# grid size
SIZE = 20

x_end = int(input("Enter x: "))
y_end = int(input("Enter y: "))

y = SIZE
while y >= 0:
    x = 0
    while x <= SIZE:
        if x_end == 0:
            # vertical line
            if x == 0:
                print("#", end="")
            else:
                print(".", end="")
        else:
            # distance from the line ax - by = 0 (scaled)
            if abs(y * x_end - x * y_end) <= max(x_end, y_end) / 2:
                print("#", end="")
            else:
                print(".", end="")
        x = x + 1
    print()
    y = y - 1
