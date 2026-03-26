# Mandi Price Checker

A simple desktop application to check vegetable prices from the mandi (market) using a graphical user interface.

## Features

- **Check Prices**: Look up real-time prices for vegetables per kilogram
- **Add Items**: Dynamically add new vegetables to the price list
- **Remove Items**: Remove vegetables from the list
- **Clean UI**: User-friendly interface built with Tkinter
- **Async Processing**: Non-blocking price fetching with threading

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## Installation

1. Clone or download this repository
2. Ensure Python 3.x is installed on your system
3. No additional dependencies required (tkinter is built-in)

## Usage

1. Run the application:
```bash
python app.py
```

2. **Check Price**:
   - Select a vegetable from the dropdown or type a name
   - Click "Check Price" button
   - Wait for the mandi rate to appear

3. **Add Item**:
   - Type a new vegetable name in the text field
   - Click "Add Item" button
   - The item will be added to the dropdown list

4. **Remove Item**:
   - Select the vegetable you want to remove
   - Click "Remove Item" button
   - The item will be removed from the list

## Default Items

- Potato
- Onion
- Tomato

## Application Structure

The app is built around the `MandiPriceApp` class which handles:
- **UI Setup**: Creating buttons, dropdowns, and labels
- **Item Management**: Adding and removing vegetables
- **Price Fetching**: Simulating API calls and displaying results
- **Threading**: Preventing UI freezing during price lookup

## How It Works

- Prices are randomly generated between ₹15 to ₹40 per kg (simulated data)
- The app includes a 1.5-second delay to simulate actual network calls
- Threading ensures the UI remains responsive during price fetching

## Future Enhancements

- Integration with real mandi API for live prices
- Display price history and trends
- Filter by region/mandi location
- Save favorite vegetables
- Price comparison across different mandis
