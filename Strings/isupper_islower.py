text = input("Jaký text chceš zkontrolovat? ")

#Simple 'If' statement resolving text user input is a) either lowercase, b) uppercase, c) mishmash or a d) random characters (not supported)
#if text.isupper():
#    print(f"Dobrá práce, celý text je velkými znaky! A vypadá takto: {text}")
#elif text.islower():
#    print(f"Dobrá práce, celý text je malými znaky! A vypadá takto: {text}")
#elif text.islower() & text.isupper() == False:
#    print(f"Text je bohužel splácanina náhodných znaků, vyber si příště text co je velkými, nebo malými, napsal jsi totiž: {text}")
#else:
#    print(f"Bratře můj v Kristu, toto není text! Napsal jsi toto: {text} a tomu já nerozumím :/")

print(f"Celý text je napsaný malými znaky? {text.lower() == text}")
print(f"Celý text je napsaný velkými znaky? {text.upper() == text}")
