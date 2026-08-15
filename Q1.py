# ================ Code here =================
class HotelRoom():
    def __init__(self, room_id, room_type, price_per_night, nights):
        self.room_id = str(room_id)
        self.room_type = str(room_type)
        self.price_per_night = int(price_per_night)
        self.nights = int(nights)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights
        return total

    def display_info(self):
         return f"{self.room_id} {self.room_type} price={self.price_per_night} nights={self.nights}" 

class StandardRoom(HotelRoom):
    def __init__(self, room_id, price_per_night, nights):
        super().__init__(room_id, "StandardRoom", price_per_night, nights)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights
        return total

    def display_info(self):
         return f"{self.room_id} {self.room_type} price={self.price_per_night} nights={self.nights}" 

class DeluxeRoom(HotelRoom):
    def __init__(self, room_id, price_per_night, nights, service_fee):
        super().__init__(room_id, "DeluxeRoom", price_per_night, nights)
        self.service_fee = int(service_fee)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights + self.service_fee
        return total

    def display_info(self):
         return f"{self.room_id} {self.room_type} price={self.price_per_night} nights={self.nights} service_fee={self.service_fee}" 

class SuiteRoom(HotelRoom):
    def __init__(self, room_id, price_per_night, nights, service_fee, luxury_tax):
        super().__init__(room_id, "SuiteRoom", price_per_night, nights)
        self.service_fee = int(service_fee)
        self.luxury_tax = int(luxury_tax)

    # --Methods
    def calculate_total(self):
        total = 0
        total = self.price_per_night * self.nights + self.service_fee + self.luxury_tax
        return total

    def display_info(self):
         return f"{self.room_id} {self.room_type} price={self.price_per_night} nights={self.nights} service_fee={self.service_fee} luxury_tax={self.luxury_tax}" 
    
# ============================================

# ===============Do not edit the code below================
def main() -> None:
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
