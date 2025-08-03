import tkinter as tk
from tkinter import messagebox
import csv
import datetime
import os

file = "attendance.csv"

def mark():
    roll = e1.get().strip()
    name = e2.get().strip()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    if not roll or not name:
        messagebox.showwarning("Error", "Enter roll and name")
        return
    # Check if attendance already marked for today
    if os.path.exists(file):
        with open(file) as f:
            if any(row[0] == roll and row[2] == date for row in csv.reader(f) if row):
                messagebox.showinfo("Info", "Already marked today")
                return
    # Write header if file does not exist
    header = not os.path.exists(file)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(["Roll No", "Name", "Date", "Status"])
        writer.writerow([roll, name, date, "Present"])
    messagebox.showinfo("Success", f"Marked present: {name}")
    e1.delete(0, tk.END)
    e2.delete(0, tk.END)

def show():
    if not os.path.exists(file):
        messagebox.showerror("Error", "No records found")
        return
    with open(file) as f:
        data = f.read()
    top = tk.Toplevel()
    top.configure(bg="#e0f7fa")
    top.title("Attendance Records")
    tk.Label(top, text=data, justify="left", font=("Courier", 10), bg="#e0f7fa").pack()

root = tk.Tk()
root.title("Attendance Manager")    # App title updated here
root.configure(bg="#e0f7fa")
tk.Label(root, text="Attendance Manager", font=("Arial", 16, "bold"), bg="#e0f7fa", fg="#00796b").grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Roll No", font=("Arial", 11), bg="#e0f7fa").grid(row=1, column=0)
tk.Label(root, text="Name", font=("Arial", 11), bg="#e0f7fa").grid(row=2, column=0)
e1 = tk.Entry(root)
e2 = tk.Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
tk.Button(root, text="Mark Present", command=mark, bg="#b2dfdb", font=("Arial", 10, "bold")).grid(row=3, column=0, pady=10)
tk.Button(root, text="Show Attendance", command=show, bg="#ffe082", font=("Arial", 10, "bold")).grid(row=3, column=1, pady=10)

root.mainloop()
