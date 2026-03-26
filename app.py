import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import threading


root = tk.Tk()
root.title("Mandi Price App")
root.geometry("400x350")


veg_list = ["Potato", "Onion", "Tomato"]


def add_item():
    name = entry.get()
    name = name.strip().title()

    if name == "":
        messagebox.showwarning("Error", "Enter something")
        return

    if name in veg_list:
        messagebox.showinfo("Info", "Already exists")
    else:
        veg_list.append(name)
        combo["values"] = veg_list
        messagebox.showinfo("Done", "Added")


def remove_item():
    name = entry.get()
    name = name.strip().title()

    if name in veg_list:
        veg_list.remove(name)
        combo["values"] = veg_list
        messagebox.showinfo("Removed", "Deleted")
    else:
        messagebox.showwarning("Error", "Not found")


def get_price():
    item = entry.get().strip()

    if item == "":
        messagebox.showwarning("Error", "Select item")
        return

    btn.config(text="Loading...", state="disabled")
    result_label.config(text="Please wait...")

    t = threading.Thread(target=process, args=(item,))
    t.start()


def process(item):
    time.sleep(1.5)

    if item.title() in veg_list:
        price = random.randint(1500, 4000) / 100
        text = item.title() + " price is ₹" + str(price) + " per kg"
    else:
        text = "No data found"

    root.after(0, show_result, text)


def show_result(text):
    result_label.config(text=text)
    btn.config(text="Check Price", state="normal")


label = tk.Label(root, text="Mandi Price Checker", font=("Arial", 16))
label.pack(pady=10)

entry = tk.StringVar()

combo = ttk.Combobox(root, textvariable=entry, values=veg_list)
combo.pack(pady=10)
combo.set("Potato")

add_btn = tk.Button(root, text="Add", command=add_item)
add_btn.pack(pady=5)

remove_btn = tk.Button(root, text="Remove", command=remove_item)
remove_btn.pack(pady=5)

btn = tk.Button(root, text="Check Price", command=get_price)
btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)


root.mainloop()
