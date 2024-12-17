def print_hello_world():
    print("Hello world from inside the function!")

# Calling print_hello_world()
print_hello_world()
print_hello_world()

# Function definition of greet_by_name (name)
def greet_by_name(name):
    print(f"Hello, {name}")

# Call function greet_by_name (name) with "John" as the name argument
greet_by_name("John")
greet_by_name("Albert")

def print_full_name(name, surname):
    print(f"{name} {surname}")

# Calling a function without specifying thr parameter names
print_full_name("Jon", "Snow")
print_full_name("Stanis", "Baratheon")

#Výstupy
greet_by_name("Lenka")
greet_by_name('František')
print_full_name("Karel", "Gott")
print_full_name("Leona",  "Macháčková")
print_hello_world()
print_full_name("Patricie",  "Stavová")

def print_vetsi(cislo1, cislo2):
    if cislo1 > cislo2:
        print(f"Větší číslo je: {cislo1}")
    elif cislo2 > cislo1:
        print(f"Větší číslo je: {cislo2}")
    else:
        print("Obě čísla jsou stejná.")


print_vetsi(20, 89)