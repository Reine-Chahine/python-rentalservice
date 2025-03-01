class user:
    def __init__(self, brand, model, year, rental_price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self._rental_price_per_day = rental_price_per_day

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Rental Price: ${self._rental_price_per_day}/day")

    def calculate_rental_cost(self, days):
        return self._rental_price_per_day * days

    def get_rental_price_per_day(self):
        return self._rental_price_per_day
     
    def set_rental_price_per_day(self, price):
        if price > 0:
            self._rental_price_per_day = price
        else:
            print("error")