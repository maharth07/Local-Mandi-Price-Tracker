# 🛒 Local Mandi Price Tracker

A simple and intuitive GUI application to check hyper-local vegetable prices in real-time. Perfect for consumers who want to know fair market prices before visiting local mandis (farmer markets).

## 📋 Features

- **Live Price Checking**: Search for vegetable prices with a single click
- **Dynamic Item Management**: Add and remove vegetables from the tracking list
- **User-Friendly Interface**: Clean, modern Tkinter GUI with intuitive controls
- **Real-Time Updates**: Get timestamps for when prices were last updated
- **Non-Blocking UI**: Uses threading to keep the interface responsive during price fetches
- **Pre-Loaded Suggestions**: Comes with common vegetables (Potato, Onion, Tomato, etc.)
- **Keyboard Support**: Press Enter to quickly search for prices

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- Windows, macOS, or Linux

### Required Libraries

Install the required dependencies using pip:

```bash
pip install requests beautifulsoup4
```

If you're using a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On macOS/Linux

pip install requests beautifulsoup4
```

## 💻 Usage

### Running the Application

```bash
python app.py
```

Once the app launches:

1. **Select or Type a Vegetable**: Use the dropdown combobox to select from the suggested list or type a custom vegetable name
2. **Add New Items**: Click the `+` button to add custom vegetables to your tracking list
3. **Remove Items**: Click the `-` button to remove vegetables you're no longer tracking
4. **Check Prices**: Click the "Check Price" button (or press Enter) to fetch the latest price
5. **View Results**: The price will display below with a timestamp

### Example Workflow

```
1. Open the app
2. Select "Tomato" from dropdown (or type "Broccoli")
3. Click "+" to add "Broccoli" to your list
4. Change selection to "Broccoli"
5. Click "Check Price"
6. View result: "✅ Success! Broccoli: ₹25.50 per kg (Updated: 3:45 PM)"
```

## 🏗️ Code Structure

### Class: `MandiTrackerApp`

The main application class that manages the GUI and price tracking logic.

#### **Attributes:**
- `root`: The main Tkinter window
- `item_var`: StringVar holding the currently selected/typed item
- `item_combo`: Dropdown combobox for vegetable selection
- `suggested_items`: List of vegetables to track (dynamically updated)
- `result_lbl`: Label to display price results
- `search_btn`: Button to trigger price search

#### **Key Methods:**

| Method | Purpose |
|--------|---------|
| `__init__(root)` | Initializes the GUI with all UI elements and styling |
| `add_item()` | Adds a new vegetable to the tracking list |
| `remove_item()` | Removes a vegetable from the tracking list |
| `start_scraping_thread()` | Creates a background thread to fetch prices |
| `scrape_price(item_name)` | Fetches price data for the selected item |
| `update_ui_with_result(text, color)` | Updates the display with price results |

## 🎨 UI Components

- **Header**: "🛒 Hyper-Local Price Checker"
- **Subtitle**: Instructional text
- **Input Frame**: Contains combobox + Add/Remove buttons
- **Search Button**: Green button to fetch prices
- **Result Label**: Displays prices, errors, or status messages
- **Color Scheme**: Professional blue/green/red accent colors

## ⚙️ Configuration

You can customize the app by modifying these sections in `app.py`:

```python
# Change the default market URL (future implementation)
MARKET_URL = "https://your-market-api.com"

# Modify default vegetables
self.suggested_items = ["Potato", "Onion", "Tomato", ...]

# Adjust window size
self.root.geometry("450x380")

# Change color scheme
bg="#f4f6f9"  # Background color
fg="#2c3e50"  # Text color
```

## 🔮 Current Limitations & Future Enhancements

### Current State:
- **Price Data**: Currently simulates prices with random values (₹1500-₹4000 per 100 units)
- **No Real API**: Doesn't connect to a live market price API yet

### Planned Features:
- [ ] Connect to real mandi price APIs
- [ ] Save price history and display trends
- [ ] Location-based price tracking
- [ ] Export data to CSV
- [ ] Price alerts and notifications
- [ ] Dark mode support
- [ ] Mobile app version

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Run `pip install requests beautifulsoup4` |
| GUI doesn't appear | Ensure tkinter is installed (comes with Python by default) |
| App is slow | Check your internet connection |
| Prices not updating | Verify the market URL is accessible |

## 📝 Example Output

**Success Case:**
```
✅ Success!

Potato: ₹18.50 per kg
(Updated: 3:45 PM)
```

**Error Case:**
```
❌ Not Found.

Could not find prices for 'Carrot' today.
```

**Connection Error:**
```
⚠️ Connection Error.
Make sure you are connected to the internet.
```

## 📦 Dependencies Breakdown

| Package | Purpose | Version |
|---------|---------|---------|
| `tkinter` | GUI framework (built-in) | - |
| `requests` | HTTP requests for API calls | Latest |
| `beautifulsoup4` | Web scraping (for future use) | Latest |
| `threading` | Non-blocking operations (built-in) | - |
| `datetime` | Timestamp generation (built-in) | - |

## 📄 License

This project is open-source and available for personal and commercial use.

## 👨‍💻 Author & Support

For bugs, feature requests, or questions, feel free to reach out!

---

**Last Updated**: March 2026  
**Status**: Active Development
