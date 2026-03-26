# 🛒 Mandi Price Checker

A simple GUI application to check vegetable prices from local mandis (farmer markets). Built with Python and Tkinter for easy price tracking.

## 📋 Features

- **Vegetable Selection**: Choose from a dropdown list of common vegetables
- **Dynamic List Management**: Add and remove vegetables from your tracking list
- **Price Checking**: Get simulated price information for selected items
- **Non-Blocking UI**: Uses threading to keep the interface responsive
- **Simple Interface**: Clean and straightforward design

## 🚀 Installation

### Prerequisites
- Python 3.6 or higher
- Tkinter (comes pre-installed with Python)

### Required Libraries

Install the required dependencies:

```bash
pip install tk
```

*Note: Tkinter usually comes with Python by default. If you get import errors, install it using your system's package manager.*

## 💻 Usage

### Running the Application

```bash
python app.py
```

### How to Use

1. **Select a Vegetable**: Use the dropdown to choose from available options (Potato, Onion, Tomato)
2. **Add New Items**: Type a vegetable name and click "Add" to include it in the list
3. **Remove Items**: Select an item and click "Remove" to delete it from the list
4. **Check Price**: Click "Check Price" to get the current price information
5. **View Results**: The price will be displayed below the button

### Example Workflow

```
1. Launch the app
2. Select "Potato" from dropdown
3. Click "Check Price"
4. See result: "Potato price is ₹25.30 per kg"
5. Type "Carrot" in the dropdown
6. Click "Add" to add it to the list
7. Select "Carrot" and check its price
```

## 🏗️ Code Structure

### Global Variables
- `root`: Main Tkinter window
- `veg_list`: List of available vegetables (dynamically updated)

### Functions

| Function | Purpose |
|----------|---------|
| `add_item()` | Adds a new vegetable to the veg_list |
| `remove_item()` | Removes a vegetable from the veg_list |
| `get_price()` | Initiates price checking in a background thread |
| `process(item)` | Simulates price fetching (runs in background) |
| `show_result(text)` | Updates the UI with price results |

### UI Components

| Component | Type | Purpose |
|-----------|------|---------|
| `label` | Label | App title |
| `combo` | Combobox | Vegetable selection dropdown |
| `add_btn` | Button | Add new vegetable |
| `remove_btn` | Button | Remove vegetable |
| `btn` | Button | Check price |
| `result_label` | Label | Display price results |

## ⚙️ Configuration

### Default Vegetables

The app starts with these vegetables:
```python
veg_list = ["Potato", "Onion", "Tomato"]
```

### Price Simulation

Prices are currently simulated using:
```python
price = random.randint(1500, 4000) / 100  # ₹15.00 - ₹40.00 per kg
```

### Window Settings

```python
root.geometry("400x350")  # Window size
root.title("Mandi Price App")  # Window title
```

## 🔮 Future Enhancements

- [ ] Connect to real mandi price APIs
- [ ] Save price history
- [ ] Export data to CSV
- [ ] Price trend analysis
- [ ] Location-based pricing
- [ ] Price alerts

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Tkinter import error | Install tkinter: `pip install tk` or use system package manager |
| App won't start | Ensure Python 3.6+ is installed |
| Buttons not working | Check if all functions are defined before UI creation |
| Threading issues | Make sure `threading` module is imported |

## 📝 Example Output

**Success Case:**
```
Potato price is ₹28.50 per kg
```

**No Data Case:**
```
No data found
```

**Error Messages:**
- "Enter something" - When trying to add empty item
- "Already exists" - When adding duplicate vegetable
- "Not found" - When trying to remove non-existent item
- "Select item" - When checking price without selection

## 📦 Dependencies

| Package | Purpose | Installation |
|---------|---------|--------------|
| `tkinter` | GUI framework | Pre-installed with Python |
| `random` | Price simulation | Built-in |
| `time` | Delays | Built-in |
| `threading` | Background processing | Built-in |

## 📄 License

This project is open-source and available for personal use.

## 👨‍💻 Author

Simple mandi price tracking application.

---

