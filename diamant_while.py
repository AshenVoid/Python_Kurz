radky = int(input("Kolik řádků? "))
#Horní část
momentalni_radek = 1
while momentalni_radek <= radky:
    mista = ''
    pocet_mezer = radky - momentalni_radek
    while pocet_mezer > 0:
        mista += ' '
        pocet_mezer -= 1

    mrizky = ''
    pocet_mrizky = 2 * momentalni_radek - 1
    while pocet_mrizky > 0:
        mrizky += '#'
        pocet_mrizky -= 1

    print(mista + mrizky)
    momentalni_radek += 1

#Dolní část
momentalni_radek = radky - 1
while momentalni_radek > 0:
    mista = ''
    pocet_mezer = radky - momentalni_radek
    while pocet_mezer > 0:
        mista += ' '
        pocet_mezer -= 1

    mrizky = ''
    pocet_mrizky = 2 * momentalni_radek - 1
    while pocet_mrizky > 0:
        mrizky += '#'
        pocet_mrizky -= 1

    print(mista + mrizky)
    momentalni_radek -= 1