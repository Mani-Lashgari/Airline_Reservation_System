# ✈️ Airline Reservation System (Python)

Airline Reservation System Management Project (Function-Oriented) in Python

This project was an educational project developed by the AIM startup for the Python Programming course. It was designed to cover various topics and help students gain practical experience in the fundamental concepts of Python programming.

#### 👨‍💻 Developers:

[Daniyal Iran Mehr](https://github.com/DaniaylIranMehr) (Supervisor)

Mani Lashgari

---

## 📚 Project Overview

This system simulates an airline reservation management platform where:

* Airline information is loaded from a file (`Airlines.txt`)
* Each airline has its own dynamic passenger list
* Routes between countries are validated using **Adjacency Matrices (Graph Representation)**
* Passengers can be added, removed, searched, and sorted
* Airlines can be searched and sorted by satisfaction rate
* Optional **Text-to-Speech mode** is supported

---

## 🏗️ Data Structures Used

* **Dictionary**

  * Used to store airlines and their passenger lists.
* **List**

  * Used for storing airline data and passenger details.
* **Adjacency Matrix**

  * Used to represent flight routes between countries.
* **Graph Concept**

  * Each airline has its own route graph.
* **Sorting with Dictionary & Lambda**

  * Airlines sorted based on satisfaction rate.

---

## 🌍 Supported Countries (Routes)

Flights are validated between the following countries:

* Emirates
* America
* Germany
* Canada

Each airline has its own adjacency matrix to determine available routes.

---

## ⚙️ Features

### 1️⃣ Add Passenger

* Validates:

  * Correct airline name
  * Correct passenger information format
  * Route availability
  * Duplicate passengers
* Prevents:

  * Invalid age (non-numeric)
  * Incorrect gender input
  * Incorrect marital status
  * Invalid routes
  * Duplicate registration

---

### 2️⃣ Remove Passenger

* Removes passenger from a selected airline.
* Shows appropriate message if:

  * Airline not found
  * Passenger not found

---

### 3️⃣ Search

#### 🔍 Search Airlines

Displays:

* Safety rate
* International status
* Satisfaction rate
* Plane capacity
* Discount availability
* First-class availability
* Airline age
* Number of employees
* Number of passengers

#### 🔍 Search Passenger

Displays:

* Airline name
* Full passenger information

---

### 4️⃣ Sort

* **Airlines:** Sorted by satisfaction rate (descending)
* **Passengers:** Sorted alphabetically by name inside a selected airline

---

### 5️⃣ Speak Mode 🎤

Using `pyttsx3`, the program supports:

* Turning voice assistant ON/OFF
* Audio guidance for menu navigation

---

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Install required dependency:

```bash
pip install pyttsx3
```

3. Run the program:

```bash
python main.py

```

---

## 📌 Notes

* Passenger capacity is considered unlimited.
* Data is read from file at startup.
* All validations are handled inside the system.
* Routes differ for each airline.
