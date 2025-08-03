# 📋 Attendance Manager (Tkinter GUI)

> "Attendance may not define your future, but it sure defines your present."

A simple yet functional **Attendance Manager App** built using Python and Tkinter. Record, store, and view student attendance with a smooth UI and local CSV storage.

---

## 🚀 Features

- ✅ Mark student present by Roll No and Name
- 📅 Automatically captures current date
- 🧠 Prevents duplicate marking for the same day
- 📁 Stores attendance data in `attendance.csv`
- 👁 View attendance records in a scrollable window
- 🎨 Minimal pastel UI with clear labels and buttons

---

## 🛠 Tech Stack

- **Language**: Python 3.x  
- **Library**: Tkinter (for GUI)  
- **Storage**: CSV file (`attendance.csv`)  
- **Date Handling**: `datetime` module

---

## 📦 Setup Instructions

### Requirements

- Python 3.x

### How to Run

1. Save the script as `attendance_manager.py`
2. Run using:

bash
python attendance_manager.py
`

---

## 🧠 How It Works

* User enters **Roll No** and **Name**, then clicks **Mark Present**
* The app checks if attendance for that roll number is already marked for **today**
* If not marked, the record is saved in `attendance.csv` with the status "Present"
* Clicking **Show Attendance** opens a new window showing all saved entries

CSV file format:


Roll No | Name | Date | Status


---

## 🖼 UI Overview

* Top Label: "Attendance Manager"
* Input Fields: Roll No & Name
* Buttons:

  * `Mark Present` — marks current day's attendance
  * `Show Attendance` — displays all saved entries

---

## 📜 License

Free to use, modify, and learn from.
Use responsibly and stay present. 😉

---

## 🙌 Author

Made with 🌟 by **RAM RAMESH YADAV**
Roll No.: 38
Department: Computer Engineering
College: \[DILKAP]

---

Have fun building more features — like filtering by date, exporting to Excel, or integrating face recognition! 🔥

```
