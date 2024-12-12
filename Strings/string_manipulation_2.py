str = "qsxht!trfecdtcbgřáýčerdxdpsěš d21rřcřetčěpe**u?rsS"


#Playful manipulation of the string kind, just slicing and flipping in a more practical case
print(f"V tomto řetězci ignorujeme prvních 5 znaků a vypadá takto: {str[5:]}")
str = str[5:]
print(f"Otáčíme ho: {str[::-1]}")
str = str[::-1]
print(f"A vypisujeme každý 4. znak: {str[::4]}")
str = str[::4]
print(f"Teoreticky pak můžeme uložit nový string: {str}")


