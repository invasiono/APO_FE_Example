Students complete the assignment directly in the Qx.py files within the given project. 
When submitting, create an empty folder, copy the Qx.py files into that folder, and then submit it to the testing software.
Q1(3.0 points)
Students code directly at the specified location in a file named Q1.py within the given project.
Create a Python program to demonstrate inheritance and polymorphism using a hotel room management scenario.
1. Build the parent class HotelRoom (0.5 points)
Create a HotelRoom class that stores the common information of a room booking:
• room_id: room code
• room_type: room type
• price_per_night: price per night
• nights: number of nights booked
The HotelRoom class must include the following methods:
• calculate_total(): returns the total payment amount for the room booking
• display_info(): returns the room information as a formatted string
2. Build the child classes (2.5 points)
Create 3 child classes that inherit from HotelRoom:
The StandardRoom has no additional fee. The total payment is calculated using the formula: total = price_per_night * nights. The returned information must follow this exact format:
R001 StandardRoom price=500000 nights=2
The DeluxeRoom has an additional service_fee. The total payment is calculated using the formula: total = price_per_night * nights + service_fee. The returned information must follow this exact format:
R002 DeluxeRoom price=800000 nights=3 service_fee=120000
The SuiteRoom has both service_fee and luxury_tax. The total payment is calculated using the formula: total = price_per_night * nights + service_fee + luxury_tax. The returned information must follow this exact format:
R003 SuiteRoom price=1500000 nights=2 service_fee=200000 luxury_tax=100000
The result must be produced through polymorphic method calls; do not use if/elif, type(), or isinstance() to sele:ct the calculation or display behavior.
After implementing the required classes and method overrides, run the main() function. A correct solution must produce exactly the sample output below, including all values, field order, punctuation, spacing, and string format.
Required sample data and output:
R001 StandardRoom price=500000 nights=2 -> total=1000000
R002 DeluxeRoom  price=800000 nights=3 service_fee=120000 -> total=2520000
R003 SuiteRoom   price=1500000 nights=2 service_fee=200000 luxury_tax=100000 -> total=3300000
R004 StandardRoom price=450000 nights=4 -> total=1800000
R005 SuiteRoom   price=2000000 nights=1 service_fee=150000 luxury_tax=250000 -> total=2400000

Q2(4.0 points)
Students code directly at the specified location in a file named Q2.py within the given project.
Create a Python program that reads room booking data from a CSV file, reads additional fee data from a JSON file, calculates total payment, and filters rooms by total payment.
Given file: room.csv
The project contains a CSV file named room.csv with the following booking data:
booking_id,room_id,room_type,price_per_night,nights,guest_name
B001,R001,StandardRoom,50000,2,Alice Nguyen
B002,R002,DeluxeRoom,80000,3,Bob Tran
B003,R003,SuiteRoom,150000,2,Carol Le
B004,R004,StandardRoom,45000,4,David Ho
B005,R005,SuiteRoom,200000,1,Emma Pham
B006,R006,DeluxeRoom,90000,2,Frank Vo
Given file: fees.json
The project also contains a JSON file named fees.json with additional fee data for each booking:
{
  "fees": [
    {"booking_id": "B001", "service_fee": 0, "luxury_tax": 0},
    {"booking_id": "B002", "service_fee": 20000, "luxury_tax": 0},
    {"booking_id": "B003", "service_fee": 30000, "luxury_tax": 50000},
    {"booking_id": "B004", "service_fee": 0, "luxury_tax": 0},
    {"booking_id": "B005", "service_fee": 25000, "luxury_tax": 60000},
    {"booking_id": "B006", "service_fee": 15000, "luxury_tax": 0}
  ]
}
1. Load room data from the CSV file (1.0 point)
Function load_booking() reads rooms.csv and load the following fields for each room:
•   room_id: room code
•   room_type: room type
•   price_per_night: price per night
•   nights: number of nights booked
•   status: current room status
•   note: short description of the room
The program must convert price_per_night and nights to integers. After loading the data from room.csv, print each booking in the following format:
B001 R001 StandardRoom Alice Nguyen price=50000 nights=2
B002 R002 DeluxeRoom Bob Tran price=80000 nights=3
B003 R003 SuiteRoom Carol Le price=150000 nights=2
B004 R004 StandardRoom David Ho price=45000 nights=4
B005 R005 SuiteRoom Emma Pham price=200000 nights=1
B006 R006 DeluxeRoom Frank Vo price=90000 nights=2
2. Load fees.json and calculate total payment (2.0 point)
Function load_fee() reads fees.json and match each fee record to the correct booking using booking_id. For each booking, calculate the total payment using this formula:
  total = price_per_night * nights + service_fee + luxury_tax
After combining room.csv and fees.json, function print_bookings_with_total() prints each booking with service_fee, luxury_tax, and total in the following exact format:
B001 R001 StandardRoom Alice Nguyen price=50000 nights=2 service_fee=0 luxury_tax=0 -> total=100000
B002 R002 DeluxeRoom Bob Tran price=80000 nights=3 service_fee=20000 luxury_tax=0 -> total=260000
B003 R003 SuiteRoom Carol Le price=150000 nights=2 service_fee=30000 luxury_tax=50000 -> total=380000
B004 R004 StandardRoom David Ho price=45000 nights=4 service_fee=0 luxury_tax=0 -> total=180000
B005 R005 SuiteRoom Emma Pham price=200000 nights=1 service_fee=25000 luxury_tax=60000 -> total=285000
B006 R006 DeluxeRoom Frank Vo price=90000 nights=2 service_fee=15000 luxury_tax=0 -> total=195000

3. Filter bookings by total payment (1.0 point)
After calculating the total payment, function print_filtered_bookings() filters and prints only the bookings whose total payment is greater than 100000 and sort them in descending order of total value.
For each booking that satisfies the condition, print one line in the following format:
  booking_id room_id room_type guest_name total=total_payment
Expected output:
B003 R003 SuiteRoom Carol Le total=380000
B005 R005 SuiteRoom Emma Pham total=285000
B002 R002 DeluxeRoom Bob Tran total=260000
B006 R006 DeluxeRoom Frank Vo total=195000
B004 R004 StandardRoom David Ho total=180000

Q3(3.0 points)
Students code directly at the specified location in a file named Q3.py within the given project.
Create a Python Tkinter application for a simple hotel booking interface. The application must display input widgets and handle two simple button events.

1. Design a Tkinter window with the following widgets (0.5 points):
•   A window title: Hotel Booking App
•   An Entry for guest name
•   An Entry for room type
•   An Entry for number of nights
•   A Label used to display messages or results
•   A button named Add Booking
•   A button named Clear
Students may use pack(), grid(), or place() to arrange the widgets, but the interface must be clear and easy to use.
2. Add Booking button event (1.5 points)
When the user clicks the Add Booking button, the program must get the values from the three Entry widgets and display a booking message in the result Label.
If all fields are filled in, the result Label must show the following format:
  Booking added: guest_name - room_type - nights nights
For example, if the user enters Alice Nguyen, DeluxeRoom, and 3, the result Label must display:
  Booking added: Alice Nguyen - DeluxeRoom - 3 nights
If any field is empty, the result Label must display exactly:
  Please fill in all fields
3. Clear button event (1 points)
When the user clicks the Clear button, the program must clear all Entry widgets and reset the result Label.
After clicking Clear, the Entry widgets must be empty and the result Label must display exactly:
  Ready
Required behavior
A correct solution must implement the two button events using command functions in Tkinter. The program must not require keyboard input from the console.
The application should start by running the main() function. When the window first appears, the result Label should display:
  Ready


