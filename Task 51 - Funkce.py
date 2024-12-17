
def vynasob_list(seznam, cinitel=3):
    return [x * cinitel for x in seznam]

print(vynasob_list([3, 4, 1, 2]))  # [9, 12, 3, 6]
print(vynasob_list([1, 4, 1, 2]))  # [3, 12, 3, 6]
print(vynasob_list([1, 4, 1, 2], 2)) #[2, 8, 2, 4]


def pocet_parametru(*args):
    pocet = len(args)
    if pocet == 1:
        return f"{pocet} parametr"
    elif 2 <= pocet <= 4:
        return f"{pocet} parametry"
    else:
        return f"{pocet} parametrů"

print(pocet_parametru(2, 3, 4))
print(pocet_parametru(2, 3, 4, 2, 2))
