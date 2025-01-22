import os

def find_for_in_dotpy():
    for file in os.listdir("."): #složka
        if file.endswith(".py"): #.py
            try:
                with open(file, "r", encoding="utf-8") as f:
                    for line_number, line in enumerate(f, start=1): #čtení řádků
                        if "for" in line:
                            yield file, line_number, line.strip() #return - jméno, číslo řádku, obsah bez whitespace
            except (OSError, UnicodeDecodeError) as e:
                print(f"Nelze otevřít soubot {file}: {e}")

for file_name, line_num, obsah in find_for_in_dotpy():
    print(f"Soubor: {file_name}, Řádek: {line_num}, Obsah: {obsah}")