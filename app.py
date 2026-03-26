import tkinter as tk
from tkinter import messagebox, ttk
import random
import time
import threading

class MandiPriceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mandi Price App")
        self.root.geometry("400x380")
        
        
        self.veg_list = ["Potato", "Onion", "Tomato"]
        
        
        self.setup_ui()

    def setup_ui(self):
        """Builds and places all the visual elements on the screen."""
        # App Title
        title_label = tk.Label(self.root, text="Mandi Price Checker", font=("Arial", 16, "bold"))
        title_label.pack(pady=15)

        self.selected_item = tk.StringVar()
        self.selected_item.set("Potato") 

        self.combo = ttk.Combobox(self.root, textvariable=self.selected_item, values=self.veg_list)
        self.combo.pack(pady=10)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        add_btn = tk.Button(btn_frame, text="Add Item", command=self.add_item, width=10)
        add_btn.grid(row=0, column=0, padx=10)

        remove_btn = tk.Button(btn_frame, text="Remove Item", command=self.remove_item, width=10)
        remove_btn.grid(row=0, column=1, padx=10)

       
        self.check_btn = tk.Button(self.root, text="Check Price", command=self.get_price, 
                                   bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), width=15)
        self.check_btn.pack(pady=20)

        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def add_item(self):
        new_item = self.selected_item.get().strip().title()

        if not new_item:
            messagebox.showwarning("Input Error", "Please type an item to add.")
            return

        if new_item in self.veg_list:
            messagebox.showinfo("Duplicate", f"{new_item} is already in the list.")
        else:
            self.veg_list.append(new_item)
            self.combo["values"] = self.veg_list  # Update dropdown options
            self.combo.set(new_item)              # Select the newly added item
            messagebox.showinfo("Success", f"{new_item} added successfully.")

    def remove_item(self):
        item_to_remove = self.selected_item.get().strip().title()

        if item_to_remove in self.veg_list:
            self.veg_list.remove(item_to_remove)
            self.combo["values"] = self.veg_list
            self.selected_item.set("")            # Clear the entry field
            messagebox.showinfo("Success", f"{item_to_remove} removed.")
        else:
            messagebox.showwarning("Not Found", "Item not found in the list.")

    def get_price(self):
        item = self.selected_item.get().strip().title()

        if not item:
            messagebox.showwarning("Input Error", "Please select or type an item.")
            return

       
        self.check_btn.config(text="Fetching...", state="disabled")
        self.result_label.config(text="Please wait, checking mandi rates...")

        
        threading.Thread(target=self._simulate_network_call, args=(item,), daemon=True).start()

    def _simulate_network_call(self, item):
        time.sleep(1.5) 

        if item in self.veg_list:
            
            price = random.randint(1500, 4000) / 100
            
            result_text = f"{item} price is ₹{price:.2f} per kg"
        else:
            result_text = f"No data found for {item}."

        
        self.root.after(0, self.show_result, result_text)

    def show_result(self, text):
        """Restores the UI state and shows the final result."""
        self.result_label.config(text=text)
        self.check_btn.config(text="Check Price", state="normal", bg="#4CAF50")


if __name__ == "__main__":
    root = tk.Tk()
    app = MandiPriceApp(root)
    root.mainloop()
