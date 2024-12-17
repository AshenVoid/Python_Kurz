
vek = int(input("Kolik vám je? "))
if vek < 12:
    print("Jste Dítě!")
elif vek < 18:
    print("Jste Teenager!")
elif vek <= 59:
    print("Jste Dospělý!")
elif vek >= 60:
    print("Jste Senior!")
else:
    print("Nezadali jsi věk nebo jste se ještě nenarodili :/")



znamka = int(input("Tak se na to podíváme, co jsi dostal za známku? "))
if znamka == 1:
    print("Výborně")
elif znamka == 2:
    print("Chvalitebně")
elif znamka == 3:
    print("Dobře")
elif znamka == 4:
    print("Dostatečně")
elif znamka == 5:
    print("Nedostatečně")
else:
    print("Nenapsal jsi známku, stydíš se až tak moc?")



prijem = float(input("Kolik firma vydělala tento kvartál? "))
if prijem > 0:
    print("Firma je v zisku! ^.^")
elif prijem == 0:
    print("Firma je na nule! T-T")
elif prijem < 0:
    print("Brzo bude krach! >.>")
else:
    print("To není validní výdělek!")