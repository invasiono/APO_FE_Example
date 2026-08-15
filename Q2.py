# ================ Code here =================

#2.1-----
def load_bookings(room_file):
    room_list = []
    with open(room_file, "r") as file:
        next(file)
        for line in file:
            info = line.strip().split(",")

            booking_id = info[0]
            room_id = info[1]
            room_type = info[2]
            price = int(info[3])
            nights = int(info[4])
            guest_name = info[5]

            booking = (booking_id, room_id, room_type, guest_name, price, nights)
            room_list.append(booking)

    return room_list

def print_bookings(bookings):
    for i in bookings:
        print(f"{i[0]} {i[1]} {i[2]} {i[3]} Price={i[4]} Nights={i[5]}")

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

def print_bookings_with_total(bookings, fees):
    for i in bookings:
        booking_id, room_id, room_type, guest_name, price, nights = i
        fee_info = fees.get(booking_id, {"service_fee":0, "luxury_tax":0})
        service_fee = int(fee_info["service_fee"])
        luxury_tax = int(fee_info["luxury_tax"])

        total = i[4] * i[5] + service_fee + luxury_tax
        print(f"{i[0]} {i[1]} {i[2]} {i[3]} Price={i[4]} Nights={i[5]} Service_fee={service_fee} Luxury_tax={luxury_tax} -> Total = {total}")

def print_filtered_bookings(bookings, fees):
    filter_list = []
    for i in bookings:
            booking_id, room_id, room_type, guest_name, price, nights = i
            
            fee_info = fees.get(booking_id, {"service_fee":0, "luxury_tax":0})
            service_fee = int(fee_info["service_fee"])
            luxury_tax = int(fee_info["luxury_tax"])
    
            total = i[4] * i[5] + service_fee + luxury_tax
            if total > 100000:
                filter_list.append((booking_id, room_id, room_type, guest_name, total))

    filter_list.sort(key=lambda item: item[4], reverse=True)

    for i in filter_list:
        print(f"{i[0]} {i[1]} {i[2]} {i[3]} total={i[4]}")


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
