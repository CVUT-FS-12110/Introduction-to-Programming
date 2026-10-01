n = 10
even_count = 0
odd_count = 0
zero_count = 0
positive_count = 0
negative_count = 0
zero02_count = 0


def count_numbers():
    global even_count, odd_count, zero_count
    for i in (range(0, n + 1)):
        x = float(input(f"Value #{i}: "))
        if x % 2 == 0:
            even_count += 1
        elif x % 2 != 0:
            odd_count += 1
        else:
            zero_count += 1

    print(f"Even numbers: {even_count}")
    print(f"Odd numbers: {odd_count}")
    print(f"Zero numbers: {zero_count}")

def count_numbers_positve():

    global positive_count, negative_count, zero02_count

    for i in (range(0, n + 1)):
        y = float(input(f"Value #{i}: "))
        if y > 0:
            positive_count += 1
        elif y < 0:
            negative_count += 1
        else:
            zero02_count += 1

    print (f"Positive numbers: {positive_count}")
    print (f"Negative numbers: {negative_count}")
    print (f"Zero numbers: {zero02_count}")


count_numbers_positve()