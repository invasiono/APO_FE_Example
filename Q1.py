# ================ Code here =================
print("Q1------------------------------------------------------------\n")

class Hotel():
    def __init__(self):
        


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
