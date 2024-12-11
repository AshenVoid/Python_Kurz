# Program, který simuluje hru s tipováním čísla

# Přednastavený rozsah čísel
dolni_mez = 1
horni_mez = 100

# Počítač si myslí číslo, které je uprostřed zadaného rozsahu
tip = (dolni_mez + horni_mez) // 2

# Zahájení hry
print("Myslím si číslo mezi", dolni_mez, "a", horni_mez)

while True:
    # Počítač se zeptá na odpověď
    odpoved = input(f"Myslíte, že je to {tip}? Napište 'větší', 'menší' nebo 'trefa': ").lower()

    if odpoved == "trefa":
        print("Skvěle! Uhodl jsem číslo!")
        break
    elif odpoved == "větší":
        dolni_mez = tip + 1  # Zúžíme rozsah na větší čísla
    elif odpoved == "menší":
        horni_mez = tip - 1  # Zúžíme rozsah na menší čísla
    else:
        print("Neplatná odpověď. Zkuste 'větší', 'menší' nebo 'trefa'.")
        continue  # Opakuje se cyklus, pokud je odpověď neplatná

    # Počítač tipuje nové číslo uprostřed nového rozsahu
    tip = (dolni_mez + horni_mez) // 2