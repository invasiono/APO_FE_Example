# ================ Code here =================



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
