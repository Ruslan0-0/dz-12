def cycl():
    numbers = [1, 2, 3]
    i = 0
    while i < meaning:
        yield numbers[i % len(numbers)]
        i += 1


meaning = int(input(" = "))

for num in cycl():
    print(num)
