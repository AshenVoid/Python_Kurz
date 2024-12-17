data = {
    "Albus": "Brumbál",
    "Alice": {
        "age": 29,
        "hobbies": ["reading", "cycling", "gardening"],
        "contacts": {
            "email": "alice@example.com",
            "phone": "555-1234"
        }
    },
    "Bob": {
        "age": 34,
        "hobbies": ["hiking", "chess", "coding"],
        "contacts": {
            "email": "bob@example.com",
            "phone": "555-5678"
        }
    },
    "Charlie": {
        "age": 25,
        "hobbies": ["photography", "traveling", "music"],
        "contacts": {
            "email": "charlie@example.com",
            "phone": "555-9101"
        }
    },
}

print(f"Získejte hodnotu 25: {data['Charlie']['age']}")
print(f"Získejte hodnotu Brumbál: {data['Albus']}")
print(f"Získejte hodnotu 555-1234: {data["Alice"]["contacts"]["phone"]}")
print(f"Získejte hodnotu reading: {data["Alice"]["hobbies"][0]}")
print(f"Získejte hodnotu traveling: {data["Charlie"]["hobbies"][1]}")
print(f"Získejte hodnotu bob@example.com: {data["Bob"]["contacts"]["email"]}")
print(f"Získejte hodnotu 29: {data["Alice"]["age"]}")





contacts = {
    "Alice": {"email": "alice@example.com", "phone": "555-1234"},
    "Bob": {"email": "bob@example.com", "phone": "555-5678"},
    "Charlie": {"email": "charlie@example.com", "phone": "555-9101"},
    "Diana": {"email": "diana@example.com", "phone": "555-3456"}
}
#pomocí .get() získejte telefon na Charlieho. Pokud telefon neexistuje, vypište
#'Číslo není v záznamu'
print(f"Telefon na Charlieho je: {contacts.get('Charlie', {}).get('phone', 'Číslo není v záznamu')}")
#smažte "Charlie" z kontaktů
del contacts["Charlie"]
#použijte úplně stejný kód jako na řádku 9. Program nesmí vypsat chybu
print(f"Telefon na Charlieho je: {contacts.get('Charlie', {}).get('phone', 'Číslo není v záznamu')}")
#Dianě smažte telefon, ale email jí ponechejte
contacts["Diana"].pop("phone", None)


