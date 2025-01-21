
name = input("Name: ")
surname = input("Surname: ")
age = input("Age: ")
number_of_limbs = input("How many limbs do you have: ")
year_variable = "years"
good_or_bad = "% human, good job!"

if age == "1":
    year_variable = "year"


print(f"I see, your jmeno is {name} {surname} and you are {age} {year_variable} old, I can also see that you have around {number_of_limbs} limbs, now I know everything.")

percent_of_human = (int(number_of_limbs) / 4) * 100

if percent_of_human > 100:
    percent_of_human = "a goddamn alien"

if percent_of_human == "a goddamn alien":
    good_or_bad = ", the authorities were notified... RUN."

print(f"That makes you {percent_of_human}{good_or_bad}")
