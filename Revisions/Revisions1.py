import random

a = random.randint(0, 100)
b = random.randint(1, 100)
'''
while True:
    odpoved = float(input(f"Kolik je {a} // {b}? "))
    if odpoved == a // b:
        print("Správně!")
        break
    else:
        print("Špatně, zkuste to znovu.")
'''



spravna_odpoved = a // b

while True:
    try:
        odpoved = float(input(f"Kolik je {a} / {b}? Zadejte číslo: "))

        if abs(odpoved - spravna_odpoved) < 0.001:
            print("Správně! Výborně.")
            break
        else:
            print("Špatně, zkuste to znovu.")
    except ValueError:
        print("Prosím, zadejte platné číslo.")

