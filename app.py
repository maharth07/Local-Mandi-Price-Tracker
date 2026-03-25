import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
import threading
import time
from datetime import datetime

# --- CONFIGURATION ---
MARKET_URL = "https://example-market-site.com/daily-prices" 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36"
}

class MandiTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Local Mandi Price Tracker")
        self.root.geometry("450x380") # Slightly taller to fit elements comfortably
        self.root.configure(bg="#f4f6f9")
        self.root.resizable(False, False)

        style = ttk.Style()
        style.theme_use('clam')
        
        # NEW: Make the list an instance variable so it can be modified while the app runs
        self.suggested_items = ["Potato", "Onion", "Tomato", "Cabbage", "Cauliflower", "Brinjal", "Okra"]
        
        # --- UI ELEMENTS ---
        header_lbl = tk.Label(root, text="🛒 Hyper-Local Price Checker", 
                              font=("Segoe UI", 18, "bold"), bg="#f4f6f9", fg="#2c3e50")
        header_lbl.pack(pady=(20, 10))

        sub_lbl = tk.Label(root, text="Select, type, or manage your vegetable list.", 
                           font=("Segoe UI", 10), bg="#f4f6f9", fg="#7f8c8d")
        sub_lbl.pack(pady=(0, 15))

        # NEW: Create a frame to hold the combobox and the add/remove buttons side-by-side
        input_frame = tk.Frame(root, bg="#f4f6f9")
        input_frame.pack(pady=5)

        self.item_var = tk.StringVar()
        self.item_combo = ttk.Combobox(input_frame, textvariable=self.item_var, values=self.suggested_items, 
                                       font=("Segoe UI", 12), width=16)
        self.item_combo.pack(side=tk.LEFT, padx=5)
        self.item_combo.set("Potato") 

        # NEW: Add Button
        add_btn = tk.Button(input_frame, text="+", command=self.add_item,
                            font=("Segoe UI", 10, "bold"), bg="#3498db", fg="white",
                            activebackground="#2980b9", activeforeground="white",
                            relief="flat", cursor="hand2", width=3)
        add_btn.pack(side=tk.LEFT, padx=2)

        # NEW: Remove Button
        remove_btn = tk.Button(input_frame, text="-", command=self.remove_item,
                               font=("Segoe UI", 10, "bold"), bg="#e74c3c", fg="white",
                               activebackground="#c0392b", activeforeground="white",
                               relief="flat", cursor="hand2", width=3)
        remove_btn.pack(side=tk.LEFT, padx=2)

        self.search_btn = tk.Button(root, text="Check Price", command=self.start_scraping_thread,
                                    font=("Segoe UI", 12, "bold"), bg="#27ae60", fg="white",
                                    activebackground="#2ecc71", activeforeground="white",
                                    relief="flat", cursor="hand2", width=15)
        self.search_btn.pack(pady=15)

        self.result_lbl = tk.Label(root, text="", font=("Segoe UI", 14), 
                                   bg="#f4f6f9", fg="#2c3e50", justify="center")
        self.result_lbl.pack(pady=15)

        self.root.bind('<Return>', lambda event: self.start_scraping_thread())

    # --- NEW: List Management Methods ---
    def add_item(self):
        """Adds the currently typed item to the dropdown list."""
        new_item = self.item_var.get().strip().title()
        if new_item and new_item not in self.suggested_items:
            self.suggested_items.append(new_item)
            self.suggested_items.sort() # Keep the list alphabetical
            self.item_combo['values'] = self.suggested_items # Update UI
            messagebox.showinfo("Success", f"'{new_item}' has been added to your list!")
        elif new_item in self.suggested_items:
            messagebox.showinfo("Info", f"'{new_item}' is already in the list.")
        else:
            messagebox.showwarning("Warning", "Please type an item name first.")

    def remove_item(self):
        """Removes the currently typed/selected item from the dropdown list."""
        item_to_remove = self.item_var.get().strip().title()
        if item_to_remove in self.suggested_items:
            self.suggested_items.remove(item_to_remove)
            self.item_combo['values'] = self.suggested_items # Update UI
            self.item_combo.set("") # Clear the input box
            messagebox.showinfo("Success", f"'{item_to_remove}' has been removed from your list.")
        else:
            messagebox.showwarning("Warning", f"'{item_to_remove}' is not in your saved list.")

    # --- Existing Methods ---
    def start_scraping_thread(self):
        item_to_check = self.item_var.get().strip()
        
        if not item_to_check:
            messagebox.showwarning("Input Error", "Please enter or select an item!")
            return

        self.search_btn.config(text="Searching...", state=tk.DISABLED, bg="#95a5a6")
        self.result_lbl.config(text=f"Fetching latest rates for {item_to_check}...\nPlease wait.", fg="#f39c12")

        thread = threading.Thread(target=self.scrape_price, args=(item_to_check,))
        thread.daemon = True 
        thread.start()

    def scrape_price(self, item_name):
        try:
            time.sleep(1.5) 
            
            import random
            # UPDATED: Now checks against the dynamic self.suggested_items list
            if item_name.title() in self.suggested_items:
                found_price = random.randint(1500, 4000) 
            else:
                found_price = None

            if found_price:
                price_kg = found_price / 100
                current_time = datetime.now().strftime("%I:%M %p") 
                result_text = f"✅ Success!\n\n{item_name.title()}: ₹{price_kg:.2f} per kg\n(Updated: {current_time})"
                color = "#27ae60" 
            else:
                result_text = f"❌ Not Found.\n\nCould not find prices for '{item_name}' today."
                color = "#e74c3c" 
                
            self.root.after(0, self.update_ui_with_result, result_text, color)

        except Exception as e:
            error_msg = f"⚠️ Connection Error.\nMake sure you are connected to the internet."
            self.root.after(0, self.update_ui_with_result, error_msg, "#e74c3c")

    def update_ui_with_result(self, text, color):
        self.result_lbl.config(text=text, fg=color)
        self.search_btn.config(text="Check Price", state=tk.NORMAL, bg="#27ae60")


if __name__ == "__main__":
    root = tk.Tk()
    app = MandiTrackerApp(root)
    root.mainloop()