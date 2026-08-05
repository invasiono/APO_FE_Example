Students complete the assignment directly in the Qx.py files within the given project.
When submitting, create an empty folder, copy the Qx.py files into that folder, and then submit it to the testing software.

General environment
- Target Python version: 3.8+.
- Files are UTF-8 encoded.
- Each exercise must provide a main() function and the program must start by running main().
- Outputs must match the exact text, spacing, punctuation, and line order shown in the samples below (the autograder checks exact matches).
- If an exercise refers to files in the project, those files (room.csv, fees.json, etc.) are in the project root.

Q1 (3.0 points)
Students code directly at the specified location in a file named Q1.py within the given project.

Goal: Demonstrate inheritance and polymorphism using a hotel room management scenario.

1. Build the parent class HotelRoom (0.5 points)
- Create a HotelRoom class that stores the common information of a room booking:
  - room_id: room code (string)
  - room_type: room type (string)
  - price_per_night: price per night (integer)
  - nights: number of nights booked (integer)
- The HotelRoom class must include the following methods:
  - calculate_total(self): returns the total payment amount for the room booking (int)
  - display_info(self): returns the room information as a formatted string

2. Build the child classes (2.5 points)
- Create three child classes that inherit from HotelRoom, overriding methods where appropriate:
  - StandardRoom: no additional fees.
    - total = price_per_night * nights
    - display_info example format:
      R001 StandardRoom price=500000 nights=2
  - DeluxeRoom: has an additional service_fee (integer).
    - total = price_per_night * nights + service_fee
    - display_info example format:
      R002 DeluxeRoom price=800000 nights=3 service_fee=120000
  - SuiteRoom: has service_fee and luxury_tax (integers).
    - total = price_per_night * nights + service_fee + luxury_tax
    - display_info example format:
      R003 SuiteRoom price=1500000 nights=2 service_fee=200000 luxury_tax=100000
- Use polymorphism: implement calculate_total and display_info so that calling those methods on a HotelRoom reference (or a list of mixed rooms) produces the correct behavior. Do not use if/elif, type(), or isinstance() to select behavior.

Required sample run
- After implementing the classes, implement and run main() to produce exactly the following output (each line must match exactly, including spacing):

R001 StandardRoom price=500000 nights=2 -> total=1000000
R002 DeluxeRoom  price=800000 nights=3 service_fee=120000 -> total=2520000
R003 SuiteRoom   price=1500000 nights=2 service_fee=200000 luxury_tax=100000 -> total=3300000
R004 StandardRoom price=450000 nights=4 -> total=1800000
R005 SuiteRoom   price=2000000 nights=1 service_fee=150000 luxury_tax=250000 -> total=2400000

Notes
- The extra spaces in the sample (e.g., multiple spaces after type) are intentional to match the grader's expected strings. Match the sample exactly.

Q2 (4.0 points)
Students code directly at the specified location in a file named Q2.py within the given project.

Goal: Read booking data from a CSV, read fees from a JSON file, compute totals, and filter bookings.

Provided files
- room.csv (project root) with these rows and header:
  booking_id,room_id,room_type,price_per_night,nights,guest_name
  B001,R001,StandardRoom,50000,2,Alice Nguyen
  B002,R002,DeluxeRoom,80000,3,Bob Tran
  B003,R003,SuiteRoom,150000,2,Carol Le
  B004,R004,StandardRoom,45000,4,David Ho
  B005,R005,SuiteRoom,200000,1,Emma Pham
  B006,R006,DeluxeRoom,90000,2,Frank Vo

- fees.json (project root) with this structure:
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
- Implement load_booking() to read room.csv and return a list (or dict) of bookings with at least these fields per booking:
  - booking_id (string)
  - room_id (string)
  - room_type (string)
  - price_per_night (int)
  - nights (int)
  - guest_name (string)
- Convert price_per_night and nights to integers.
- After loading, print each booking in this exact format (one line per booking), in the same order as the CSV:

B001 R001 StandardRoom Alice Nguyen price=50000 nights=2
B002 R002 DeluxeRoom Bob Tran price=80000 nights=3
B003 R003 SuiteRoom Carol Le price=150000 nights=2
B004 R004 StandardRoom David Ho price=45000 nights=4
B005 R005 SuiteRoom Emma Pham price=200000 nights=1
B006 R006 DeluxeRoom Frank Vo price=90000 nights=2

2. Load fees.json and calculate total payment (2.0 points)
- Implement load_fee() to read fees.json and match each fee record to the correct booking using booking_id.
- For each booking, calculate total using:
  total = price_per_night * nights + service_fee + luxury_tax
- Implement print_bookings_with_total() to print each booking in this exact format:

B001 R001 StandardRoom Alice Nguyen price=50000 nights=2 service_fee=0 luxury_tax=0 -> total=100000
B002 R002 DeluxeRoom Bob Tran price=80000 nights=3 service_fee=20000 luxury_tax=0 -> total=260000
B003 R003 SuiteRoom Carol Le price=150000 nights=2 service_fee=30000 luxury_tax=50000 -> total=380000
B004 R004 StandardRoom David Ho price=45000 nights=4 service_fee=0 luxury_tax=0 -> total=180000
B005 R005 SuiteRoom Emma Pham price=200000 nights=1 service_fee=25000 luxury_tax=60000 -> total=285000
B006 R006 DeluxeRoom Frank Vo price=90000 nights=2 service_fee=15000 luxury_tax=0 -> total=195000

Notes and edge handling:
- If fees.json contains a booking_id not present in room.csv, you may ignore it.
- If room.csv contains a booking_id with no corresponding fees entry, assume service_fee=0 and luxury_tax=0.
- If numeric conversion fails for price_per_night or nights, the program should raise an informative exception (the grader expects valid data for provided files).
- Maintain the same order as the CSV when printing the combined book+fee list.

3. Filter bookings by total payment (1.0 point)
- Implement print_filtered_bookings() to print bookings whose total payment is greater than 100000.
- Sort these bookings in descending order of total payment (largest first).
- Print each matching booking in this exact format:

booking_id room_id room_type guest_name total=total_payment

- Expected exact output for the provided files:

B003 R003 SuiteRoom Carol Le total=380000
B005 R005 SuiteRoom Emma Pham total=285000
B002 R002 DeluxeRoom Bob Tran total=260000
B006 R006 DeluxeRoom Frank Vo total=195000
B004 R004 StandardRoom David Ho total=180000

Q2 implementation notes
- Use the CSV header to parse fields (do not assume fixed column indices unless you check header).
- Keep output ordering deterministic: use the CSV order for the first two print lists, and a sort by total (descending) for the filtered list.

Q3 (3.0 points)
Students code directly at the specified location in a file named Q3.py within the given project.

Goal: Create a small Tkinter GUI for hotel booking input with two button handlers.

1. Window and widgets (0.5 points)
- Window title: "Hotel Booking App"
- Entry for guest name
- Entry for room type
- Entry for number of nights
- A Label to display messages or results
- A button labeled "Add Booking"
- A button labeled "Clear"
- Layout may use pack(), grid(), or place().

2. Add Booking button event (1.5 points)
- When the user clicks Add Booking, retrieve the three Entry values and display a booking message in the result Label.
- If all fields are filled, show exactly:
  Booking added: guest_name - room_type - nights nights
  Example:
  Booking added: Alice Nguyen - DeluxeRoom - 3 nights
- If any field is empty, show exactly:
  Please fill in all fields

3. Clear button event (1.0 point)
- When the user clicks Clear:
  - Clear all Entry widgets (make them empty).
  - Reset the result Label to exactly:
    Ready

Required behavior and additional notes
- Do not require or read console input (no input() calls).
- Implement the two button callbacks using Tkinter command functions.
- The application should start by running main(), and when the window first appears the result Label must display exactly: Ready
- It is acceptable (but not required) to validate that number of nights is a positive integer. If you validate it, provide a clear message if invalid — otherwise assume test inputs are valid.

Assumptions, testing, and grader notes
- The autograder will run each Qx.py and compare stdout and (for Q3) may verify behavior by launching the GUI and checking labels (or the grader may run the GUI manually).
- For deterministic outputs, adhere exactly to the sample outputs, including spacing.
- Be explicit about currency/units when relevant. Q1 and Q2 use independent sample datasets; if you want to standardize units across exercises, document that explicitly.
