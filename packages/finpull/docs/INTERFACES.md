# FinPull Interface Documentation

## Table of Contents

- [Graphical User Interface (GUI)](#graphical-user-interface-gui)
- [Command Line Interface (CLI)](#command-line-interface-cli)
- [API Interface](#api-interface)
- [Web Integration](#web-integration)
- [Examples](#examples)

## Graphical User Interface (GUI)

The desktop application provides an interactive interface for managing financial data.

### Features

- **Data Grid**: Complete view of all 27+ financial metrics
- **Multi-Selection**: Select and manage multiple tickers simultaneously
- **Real-time Updates**: Progress indicators for all operations
- **Smart Sorting**: Click column headers to sort by any metric
- **Export Options**: Save data to JSON, CSV, or Excel formats
- **Status Indicators**: Visual feedback for loading, success, and error states

### Launching the GUI

```bash
# Default launch
finpull

# Explicit GUI mode
finpull --gui
```

### GUI Components

#### Main Data Grid

The main grid displays all tracked tickers with the following columns:

- **ticker**: Stock symbol with status indicators (🔄 loading, ✅ success, ❌ error)
- **company_name**: Full company name
- **sector**: Business sector classification
- **price**: Current stock price
- **change_5y**: 5-year price change percentage
- **dividend_yield**: Dividend yield percentage
- **dividend_ttm**: Dividend per share (trailing twelve months)
- **eps_ttm**: Earnings per share (trailing twelve months)
- **eps_next_year**: Projected earnings per share (next year)
- **eps_next_5y**: Projected earnings growth (next 5 years)
- **revenue**: Total revenue
- **revenue_growth_5y**: Revenue growth (5 years)
- **operating_margin**: Operating margin percentage
- **profit_margin**: Profit margin percentage
- **roa**: Return on assets percentage
- **roe**: Return on equity percentage
- **roi**: Return on investment percentage
- **pe_ratio**: Price-to-earnings ratio
- **ps_ratio**: Price-to-sales ratio
- **pb_ratio**: Price-to-book ratio
- **total_assets**: Total company assets
- **total_liabilities**: Total company liabilities
- **market_cap**: Market capitalization
- **volume**: Current trading volume
- **avg_volume**: Average trading volume
- **beta**: Beta coefficient
- **timestamp**: Data timestamp

#### Control Panel

- **Add Ticker**: Text field for entering ticker symbols (supports space/comma separation)
- **Add Button**: Add entered tickers to tracking
- **Remove Selected**: Remove selected tickers from tracking
- **Refresh**: Update data for all tickers
- **Export**: Save data to various formats

#### Status Bar

Shows current operation status and ticker count.

### GUI Operations

#### Adding Tickers

1. Enter ticker symbols in the text field (e.g., "AAPL GOOGL MSFT")
2. Click "Add" button
3. Progress indicators show loading status
4. New rows appear in the grid

#### Removing Tickers

1. Select one or more rows in the grid
2. Click "Remove Selected" button
3. Confirm deletion when prompted

#### Sorting Data

1. Click any column header to sort by that metric
2. Click again to reverse sort order
3. Smart sorting handles different data types (numbers, percentages, text)

#### Exporting Data

1. Click "Export" button
2. Choose file location and format in dialog
3. Supported formats: JSON, CSV, Excel (XLSX)

## Command Line Interface (CLI)

The CLI provides both interactive and direct command modes for automation and scripting.

### Interactive Mode

```bash
finpull --interactive
```

Launches an interactive shell with prompt:

```
finpull> add AAPL GOOGL
finpull> show AAPL
finpull> export data.json --json
finpull> exit
```

### Direct Commands

Execute single commands directly:

```bash
finpull add AAPL GOOGL MSFT
finpull show AAPL --full
finpull refresh
finpull export portfolio --csv --json --xlsx
```

### Available Commands

#### add

Add ticker symbols for tracking.

**Syntax:**
```bash
finpull add <ticker1> [ticker2] [ticker3] ...
```

**Examples:**
```bash
finpull add AAPL
finpull add AAPL GOOGL MSFT AMZN
```

#### remove

Remove tickers from tracking.

**Syntax:**
```bash
finpull remove <ticker1> [ticker2] [ticker3] ...
```

**Examples:**
```bash
finpull remove AAPL
finpull remove AAPL GOOGL
```

#### show

Display ticker information.

**Syntax:**
```bash
finpull show [ticker] [--full]
```

**Options:**
- `--full`: Show all available data fields
- No ticker: Show all tracked tickers

**Examples:**
```bash
finpull show                   # Show all tickers (summary)
finpull show AAPL              # Show AAPL summary
finpull show AAPL --full       # Show AAPL detailed data
finpull show --full            # Show all tickers with full data
```

#### refresh

Update data from external sources.

**Syntax:**
```bash
finpull refresh [ticker]
```

**Examples:**
```bash
finpull refresh               # Refresh all tickers
finpull refresh AAPL          # Refresh specific ticker
```

#### export

Save data to files.

**Syntax:**
```bash
finpull export <filename> [--json] [--csv] [--xlsx]
```

**Options:**
- `--json`: Export to JSON format
- `--csv`: Export to CSV format
- `--xlsx`: Export to Excel format
- Multiple formats can be specified simultaneously

**Examples:**
```bash
finpull export portfolio --json
finpull export data --csv --xlsx
finpull export backup --json --csv --xlsx
```

#### stats

Show system statistics.

**Syntax:**
```bash
finpull stats
```

**Output:**
- Total tickers tracked
- Sector distribution
- Last refresh time
- Storage information

#### clear

Remove all tracked data.

**Syntax:**
```bash
finpull clear
```

**Note:** Requires confirmation prompt.

### CLI Options

#### Global Options

- `--interactive`: Launch interactive mode
- `--gui`: Launch GUI mode
- `--version`: Show version information
- `--help`: Show help information

#### Output Formatting

The CLI uses formatted tables for data display:

```
┌──────────┬─────────────────┬─────────────┬───────────┐
│ Ticker   │ Company         │ Price       │ P/E Ratio │
├──────────┼─────────────────┼─────────────┼───────────┤
│ AAPL     │ Apple Inc.      │ $150.00     │ 25.5      │
│ GOOGL    │ Alphabet Inc.   │ $2,800.00   │ 22.1      │
└──────────┴─────────────────┴─────────────┴───────────┘
```

## API Interface

Complete programmatic access for integration with other applications.

### High-Level API

```python
from finpull import FinancialDataAPI

api = FinancialDataAPI()

# Add tickers
result = api.add_ticker("AAPL")
batch_result = api.batch_add_tickers(["GOOGL", "MSFT", "TSLA"])

# Get data
data = api.get_data("AAPL")
all_data = api.get_data()

# Refresh data
api.refresh_data()

# Export data
api.export_data("json", "portfolio.json")
```

### Low-Level Scraper

```python
from finpull import FinancialDataScraper

scraper = FinancialDataScraper()
scraper.add_ticker("AAPL")
data = scraper.get_ticker_data("AAPL")
```

### GUI Integration

```python
from finpull import FinancialDataGUI

# Create GUI instance
gui = FinancialDataGUI()

# Add tickers programmatically
gui.scraper.add_ticker("AAPL")
gui.refresh_display()

# Run GUI
gui.run()
```

## Web Integration

### Browser with Pyodide

```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
</head>
<body>
    <script>
        async function initFinPull() {
            let pyodide = await loadPyodide();
            await pyodide.loadPackage(["micropip"]);
            await pyodide.runPython(`
                import micropip
                await micropip.install("finpull")
                
                from finpull import FinancialDataAPI
                api = FinancialDataAPI()
                
                import js
                js.finpull_api = api
            `);
            
            // Use from JavaScript
            let result = pyodide.runPython("api.add_ticker('AAPL')");
            console.log(result);
        }
        
        initFinPull();
    </script>
</body>
</html>
```

### Node.js Integration

```javascript
const { spawn } = require('child_process');

class FinPullInterface {
    async executeCommand(args) {
        return new Promise((resolve, reject) => {
            const process = spawn('finpull', args);
            
            let stdout = '';
            let stderr = '';
            
            process.stdout.on('data', (data) => stdout += data);
            process.stderr.on('data', (data) => stderr += data);
            
            process.on('close', (code) => {
                if (code === 0) {
                    resolve(stdout.trim());
                } else {
                    reject(new Error(`Command failed: ${stderr}`));
                }
            });
        });
    }
    
    async addTicker(ticker) {
        return this.executeCommand(['add', ticker]);
    }
    
    async exportData(filename, format = 'json') {
        return this.executeCommand(['export', filename, `--${format}`]);
    }
}

// Usage
const finpull = new FinPullInterface();
finpull.addTicker('AAPL').then(result => console.log(result));
```

## Examples

### Portfolio Management Script

```python
from finpull import FinancialDataAPI

api = FinancialDataAPI()

# Build a technology portfolio
tech_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA"]
results = api.batch_add_tickers(tech_stocks)

print(f"Successfully added {results['summary']['added_count']} stocks")

# Analyze portfolio performance
portfolio_data = api.get_data()
for stock in portfolio_data['data']:
    price = stock['price']
    pe_ratio = stock['pe_ratio']
    market_cap = stock['market_cap']
    
    print(f"{stock['ticker']}: ${price} | P/E: {pe_ratio} | Cap: {market_cap}")
```

### Automated CLI Workflow

```bash
#!/bin/bash

# Daily portfolio update script
echo "Updating portfolio..."

# Add new stocks if needed
finpull add AAPL GOOGL MSFT

# Refresh all data
finpull refresh

# Generate reports
finpull export "reports/portfolio_$(date +%Y%m%d)" --json --csv --xlsx

# Show summary
finpull show --full

echo "Portfolio update complete"
```

### GUI Automation

```python
import threading
from finpull import FinancialDataGUI

def setup_gui():
    gui = FinancialDataGUI()
    
    # Pre-populate with data
    gui.scraper.add_ticker("AAPL")
    gui.scraper.add_ticker("GOOGL")
    gui.refresh_display()
    
    return gui

# Run GUI in separate thread
gui = setup_gui()
gui_thread = threading.Thread(target=gui.run)
gui_thread.start()
```

### Real-time Monitoring

```python
import time
from finpull import FinancialDataAPI

api = FinancialDataAPI()

# Add watchlist
watchlist = ["AAPL", "GOOGL", "MSFT", "TSLA"]
api.batch_add_tickers(watchlist)

while True:
    # Refresh data every 5 minutes
    api.refresh_data()
    
    # Check for significant changes
    data = api.get_data()
    for stock in data['data']:
        change_5y = float(stock['change_5y'].replace('%', ''))
        if abs(change_5y) > 10:  # More than 10% change
            print(f"Alert: {stock['ticker']} changed {change_5y}% over 5 years")
    
    time.sleep(300)  # 5 minutes
``` 