# 🏨 Hotel Booking & Management System (Python)

A comprehensive Python project demonstrating Object-Oriented Programming (OOP), Data Processing (CSV & JSON parsing), and Desktop Graphical User Interface (GUI) development using Tkinter.

---

## 📌 Project Overview

This repository contains a modular Python application built for handling hotel room operations, calculated billing, external data parsing, and user interactive booking. 

The project is structured into three main modules:
1. **OOP & Polymorphism (`Q1.py`)**: Models different room categories (`StandardRoom`, `DeluxeRoom`, `SuiteRoom`) inheriting from a base `HotelRoom` class to compute stay totals dynamically based on room rates, service fees, and luxury taxes.
2. **Data Integration & Analytics (`Q2.py`)**: Reads structured data from CSV (`room.csv`) and JSON (`fees.json`), calculates combined totals, and filters high-value room bookings.
3. **Desktop Interface (`Q3.py`)**: A GUI application built with `tkinter` enabling users to enter new guest bookings and manage input forms interactively.

---

## 🚀 Features

- **Object-Oriented Architecture**: Clean OOP hierarchy with encapsulation, method overriding, and runtime polymorphism.
- **Dynamic Cost Calculation**:
  - **Standard Room**: `Price × Nights`
  - **Deluxe Room**: `(Price × Nights) + Service Fee`
  - **Suite Room**: `(Price × Nights) + Service Fee + Luxury Tax`
- **Multi-Format Data Handling**: Seamless data reading and merging from `.csv` and `.json` files.
- **Data Filtering & Sorting**: Processes and filters bookings exceeding specified financial thresholds in descending order.
- **User-Friendly GUI**: Simple, responsive Tkinter desktop UI with input validation and clear actions.

---

## 📁 Repository Structure

```text
├── Q1.py          # Class definitions (HotelRoom, StandardRoom, DeluxeRoom, SuiteRoom) & Polymorphism test
├── Q2.py          # Data processing pipeline (CSV parsing, JSON matching, and filtering)
├── Q3.py          # Tkinter GUI implementation for hotel booking
├── room.csv       # Raw room booking dataset
└── fees.json      # Extra fee structure dataset (service fees & luxury taxes)
