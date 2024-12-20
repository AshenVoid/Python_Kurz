import string
def x(number1, number2):
    for i in range(number1, number2):
        output = ""
        if i % 3 == 0:
            output += "fizz"
        if i % 4 == 0:
            output += "xxx"
        if i % 5 == 0:
            output += "buzz"
        if i % 6 == 0:
            output += "yyy"
        if output == "":
            output = f"{i}"
        else:
            output = output.title()
        output = string.capwords(output, sep = "bu")
        print(output)

x(1, 21)

#Cyklus pro print čísel, if číslo / 3 = fizz, když 5 = buzz
#když se spojí vícero outputů, chci aby začínal velkým písmenem a ostatní byly malým
