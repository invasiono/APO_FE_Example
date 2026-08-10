# ================ Code here =================
print("\nQ2.1-----------------------\n")


#2.1-----
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
        print(f"{i[0]} {i[1]} {i[2]} {i[3]} Price={i[4]} Nights={i[5]}")

print("\nQ2.2-----------------------\n")

#2.2----
import json

fee_file = "fees.json"
def load_fees(fee_file):
    fee_dict = {}
    with open(fee_file, "r") as file:
        data = json.load(file)
    
    for i in data.get("fees", []):
        fee_dict[i["booking_id"]] = {
            "service_fee": int(i.get("service_fee", 0)),
            "luxury_tax": int(i.get("luxury_tax", 0))
        }
    return fee_dict

load_fees(fee_file)

print("\nQ2.3-----------------------\n")

fees = load_fees(fee_file)
def print_bookings_with_total(bookings, fees):
    for i in bookings:
        booking_id, room_id, room_type, guest_name, price, nights = i
        fee_info = fees.get(booking_id, {"service_fee":0, "luxury_tax":0})
        service_fee = int(fee_info["service_fee"])
        luxury_tax = int(fee_info["luxury_tax"])

        total = i[4] * i[5] + service_fee + luxury_tax
        print(f"{i[1]} {i[2]} {i[3]} Price={i[4]} Nights={i[5]} Service_fee={service_fee} Luxury_tax={luxury_tax} -> Total = {total}")

print_bookings_with_total(bookings, fees)








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
