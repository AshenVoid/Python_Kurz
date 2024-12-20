class Dish:
    def __init__(self, name, price, category, is_vegetarian):
        self.name = name
        self.price = price
        self.category = category
        self.is_vegetarian = is_vegetarian

    def __repr__(self):
        veg_status = "(vegetarian)" if self.is_vegetarian else ""
        return f"{self.name} - {self.price} $, Category: {self.category} {veg_status}"


class Menu:
    def __init__(self, restaurant_name):
        self.restaurant_name = restaurant_name
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)
        print(f"Dish '{dish.name}' was added to the menu.")

    def show_menu(self):
        if not self.dishes:
            print("Menu is empty.")
        else:
            print(f"--- Menu of {self.restaurant_name} ---")
            for dish in self.dishes:
                print(dish)

    def get_vegetarian_dishes(self):
        veg_dishes = [dish for dish in self.dishes if dish.is_vegetarian]
        if not veg_dishes:
            print("There are no vegetarian options in the menu.")
        else:
            print("Vegetarian options:")
            for dish in veg_dishes:
                print(dish)


class Order:
    def __init__(self, customer_name, payment_method):
        self.customer_name = customer_name
        self.ordered_dishes = []
        self.payment_method = payment_method
        self.discount = 0

    def add_dish(self, dish):
        self.ordered_dishes.append(dish)
        print(f"Dish '{dish.name}' has been ordered.")

    def apply_discount(self, percent):
        self.discount = percent
        print(f"A {self.discount}% discount has been added!")

    def get_total(self):
        total = sum(dish.price for dish in self.ordered_dishes)
        total_after_discount = total * (1 - self.discount / 100)
        return round(total_after_discount, 2)

    def __repr__(self):
        total = self.get_total()
        dishes_list = ", ".join(dish.name for dish in self.ordered_dishes)
        return (f"Costumer's order: {self.customer_name}\n"
                f"Ordered dishes: {dishes_list}\n"
                f"Payment method: {self.payment_method}\n"
                f"Total price after discount: {total} $")


def restaurant_menu():
    menu = Menu("Le Monsieur Appétit")

    while True:
        print("\n--- Restaurant - Menu ---")
        print("1. Menu")
        print("2. Vegetarian Options")
        print("3. Add new dishes to the Menu")
        print("4. Create a new order")
        print("5. Leave")

        choice = input("Choose: ")

        if choice == "1":
            menu.show_menu()
        elif choice == "2":
            menu.get_vegetarian_dishes()
        elif choice == "3":
            name = input("Dish name: ")
            price = float(input("Dish price (in dollars): "))
            category = input("Category of the dish: ")
            is_vegetarian = input("Is the food vegetarian (yes/no): ").lower() == "yes"
            menu.add_dish(Dish(name, price, category, is_vegetarian))
        elif choice == "4":
            customer_name = input("Customer's name: ")
            payment_method = input("Payment method (cash / card / mobile): ")
            order = Order(customer_name, payment_method)

            while True:
                menu.show_menu()
                dish_name = input("Which dish would you like to order? (or 'leave' to leave): ")
                if dish_name.lower() == "leave":
                    break

                dish = next((d for d in menu.dishes if d.name == dish_name), None)
                if dish:
                    order.add_dish(dish)
                else:
                    print("We don't serve that here.")

            discount = int(input("Get yourself a discount! (0 for no discount): "))
            order.apply_discount(discount)
            print(order)
        elif choice == "5":
            print("Thank you for visiting 'Le Monsieur Appétit', have a good day!")
            break
        else:
            print("Incorrect choice, try again!")


if __name__ == "__main__":
    restaurant_menu()
