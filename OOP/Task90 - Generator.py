'''
def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

sekvence = fibonacci()

for _ in range(int(input("Kolik kroků fibonacciho sekvence: "))):
    print(next(sekvence))


def gen(sekvence, delka):
    for i in range(len(sekvence) - delka + 1):
        yield "".join(sekvence[i:i + delka])

for segment in gen(["A","C","E","R","F","U","P"], 2):
    print(segment)

for segment in gen(["A","C","E","R"], 3):
    print(segment)


def rle_gen(sekvence):
    if not sekvence:
        return
    count = 1
    for i in range(1, len(sekvence)):
        if sekvence[i] == sekvence[i - 1]:
            count += 1
        else:
            yield f"{count}{sekvence[i - 1]}"
            count = 1
    yield f"{count}{sekvence[-1]}"

rle_output = "".join(rle_gen("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"))
print(rle_output)
'''


