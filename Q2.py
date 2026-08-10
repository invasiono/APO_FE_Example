# ================ Code here =================
print("\n[TEST]-----------------------\n")

room_file = "room.csv"
def load_bookings(room_file):
    room_list = []
    with open(room_file, "r") as file:
        next(file)
        for line in file:
            info = line.strip().split(",")

            booking_id, room_id, room_type, guest_name, price, nights = info[0], info[1], info[2], info[5], int(info[3]), int(info[4])
            obj = booking_id, room_id, room_type, guest_name, price, nights
            room_list.append(obj)

    return room_list

bookings = load_bookings(room_file)

def print_bookings(bookings):
    for i in load_bookings(room_file):
        print(f"{i[0]} {i[2]} {i[3]} Price={i[4]} Nights={i[5]}")

print_bookings(bookings)





print("\n[RESULT]-----------------------\n")

# ============================================

def main() -> None:
    room_file = "room.csv"
    fee_file = "fees.json"

    bookings = load_bookings(room_file)

    print("Loaded bookings:")
    print_bookings(bookings)

    fees = load_fees(fee_file)

    print("Bookings with total payment:")
    print_bookings_with_total(bookings, fees)

    print("Filtered bookings:")
    print_filtered_bookings(bookings, fees)


if __name__ == "__main__":
    main()
