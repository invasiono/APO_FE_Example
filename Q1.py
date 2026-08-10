# ================ Code here =================
print("\n------------------------------------------------------------\n")

class Hotel():
    def __init__(self, room_id, room_type, price_per_night, nights):
        self.room_id = str(room_id)
        self.room_type = str(room_type)
        self.price_per_night = float(price_per_night)
        self.nights = int(nights)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights
        return total

    def display_info(self):
         return f"ID: {self.room_id} | Type: {self.room_type} | P/N: {self.price_per_night} | Nights: {self.nights}" 

obj1 = Hotel("R000","Type",0,0)
print(obj1.display_info())
print(f"Price: {obj1.calculate_total()}")

class StandardRoom(Hotel):
    def __init__(self, room_id, price_per_night, nights):
        super().__init__(room_id, "StandardRoom", price_per_night, nights)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights
        return total

    def display_info(self):
         return f"ID: {self.room_id} | Type: {self.room_type} | P/N: {self.price_per_night} | Nights: {self.nights}" 

obj2 = StandardRoom("R001",50000,2)
print(obj2.display_info())
print(f"Price: {obj2.calculate_total()}")

class DeluxeRoom(Hotel):
    def __init__(self, room_id, price_per_night, nights, service_fee):
        super().__init__(room_id, "DeluxeRoom", price_per_night, nights)
        self.service_fee = float(service_fee)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights + self.service_fee
        return total

    def display_info(self):
         return f"ID: {self.room_id} | Type: {self.room_type} | P/N: {self.price_per_night} | Nights: {self.nights} | Service: {self.service_fee}" 

obj3 = DeluxeRoom("R002",10000,3,35000)
print(obj3.display_info())
print(f"Price: {obj3.calculate_total()}")

class SuiteRoom(Hotel):
    def __init__(self, room_id, price_per_night, nights, service_fee, luxury_tax):
        super().__init__(room_id, "SuiteRoom", price_per_night, nights)
        self.service_fee = float(service_fee)
        self.luxury_tax = float(luxury_tax)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights + self.service_fee + self.luxury_tax
        return total

    def display_info(self):
         return f"ID: {self.room_id} | Type: {self.room_type} | P/N: {self.price_per_night} | Nights: {self.nights} | Service: {self.service_fee} | Luxury Tax: {self.luxury_tax}" 

obj4 = SuiteRoom("R003",20000,2,15000,20000)
print(obj4.display_info())
print(f"Price: {obj4.calculate_total()}")

print("\n------------------------------------------------------------\n")

# ============================================

# ===============Do not edit the code below================
def main() -> None:
    pass
    rooms: list[HotelRoom] = [
        StandardRoom("R001", 500000, 2),
        DeluxeRoom("R002", 800000, 3, 120000),
        SuiteRoom("R003", 1500000, 2, 200000, 100000),
        StandardRoom("R004", 450000, 4),
        SuiteRoom("R005", 2000000, 1, 150000, 250000),
    ]

    # The same method calls work for every object in the list. This is
    # polymorphism: Python selects the overridden method at runtime.
    for room in rooms:
        information = room.display_info()
        total = room.calculate_total()
        print(f"{information} -> total={total:.0f}")


if __name__ == "__main__":
    main()
# =======================================================
