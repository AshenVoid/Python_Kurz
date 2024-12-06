text = "Pomocí speciálního příkazu s operátorem [] můžeme řetězec přečíst od konce?"

#Methodics of string slicing and manipulation

#Number of specified characters
print(f"V textu se znak 's' nachází {text.count(input("Který znak? "))}")

#Slice any characters and return them
print(f"Zároveň zde můžeme vidět tuto část na indexu 7 - 14: {text[7:14]}")

#Extract specified word
print(f"Při této metodice můžeme vyříznout slovo, třeba toto: {text[29:39]}")

#Every second character
print(f"Můžeme vypsat i každý druhý znak: {text[1:76:2]}")

#Or do the magic of flipping the string
print(f"Či celý text obrátit: {text[::-1]}")

