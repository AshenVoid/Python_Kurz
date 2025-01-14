class TrainUtils:
    @staticmethod
    def calculate_travel_time(distance, speed):
        if speed <= 0:
            return "Neplatná rychlost."
        return f"Délka cesty je: {distance/speed} h"

    @staticmethod
    def calculate_ticket_price(distance, base_price_per_km):
        price = distance * base_price_per_km
        return f"Cena lístku je: {round(price, 2)} Kč."


if __name__ == "__main__":
    print(TrainUtils.calculate_travel_time(100, 50))
    print(TrainUtils.calculate_travel_time(100, 0))

    print(TrainUtils.calculate_ticket_price(100, 0.5))
    print(TrainUtils.calculate_ticket_price(400, 2.73121))