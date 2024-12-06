text = "Pomocí speciálního příkazu s operátorem [] můžeme řetězec přečíst od konce?"

#Methodics of string slicing and manipulation
print(f"V textu se znak 's' nachází {text.count("s")}")
print(f"Zároveň zde můžeme vidět tuto část na indexu 7 - 14: {text[7:14]}")
print(f"Při této metodice můžeme vyříznout slovo, třeba toto: {text[29:39]}")
print(f"Můžeme vypsat i každý druhý znak: {text[1:76:2]}")
print(f"Či celý text obrátit: {text[::-1]}")