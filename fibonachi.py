def fibonachi():
    meaning_a, meaning_b = 0, 1
    while meaning_a <= enter:
        yield meaning_a
        meaning_a, meaning_b = meaning_b, meaning_a + meaning_b


enter = int(input(" = "))

for num in fibonachi():
    print(num)
