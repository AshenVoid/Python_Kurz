
name = input("Name: ")
surname = input("Surname: ")
age = input("Age: ")
number_of_limbs = input("How many limbs do you have: ")
year_variable = "years"


if age == "1":
    year_variable = "year"


print(f"I see, your name is {name} {surname} and you are {age} {year_variable} old, I can also see that you have around {number_of_limbs} limbs, now I know everything")

percent_of_human = (int(number_of_limbs) / 4) * 100

print(f"That makes you {percent_of_human}% human, good job!")