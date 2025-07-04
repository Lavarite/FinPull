# FinPull - Professional Financial Data Scraper

[![PyPI - finpull-core](https://img.shields.io/pypi/v/finpull-core?label=finpull-core&color=blue)](https://pypi.org/project/finpull-core/)
[![PyPI - finpull](https://img.shields.io/pypi/v/finpull?label=finpull&color=green)](https://pypi.org/project/finpull/)
[![Python](https://img.shields.io/pypi/pyversions/finpull)](https://pypi.org/project/finpull/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A financial data scraper that provides comprehensive stock market data through multiple interfaces.

## 🚀 Quick Start

```bash
# For web applications and APIs (lightweight)
pip install finpull-core

# For complete desktop/CLI usage
pip install finpull
```

```python
# API Usage (both packages)
from finpull_core import FinancialDataAPI

api = FinancialDataAPI()
api.add_ticker('AAPL')
data = api.get_data('AAPL')
print(f"Apple: ${data['data']['price']}")
```

```bash
# CLI Usage (full package only)
finpull add AAPL MSFT GOOGL
finpull show
finpull export --csv portfolio.csv
```

## 📦 Package Architecture

### Two Packages, One Ecosystem

| Package | Size | Use Case | Interfaces | Dependencies |
|---------|------|----------|------------|--------------|
| **finpull-core** | 21.9KB | Web apps, APIs, microservices | API only | 3 minimal |
| **finpull** | 27.2KB | Desktop, CLI, complete toolkit | API + CLI + GUI | Includes core |

### finpull-core (Lightweight)
- **Purpose**: Embedded in web applications, APIs, and microservices
- **Size**: 21.9KB wheel, 134KB installed
- **Dependencies**: requests, beautifulsoup4, yfinance
- **Interfaces**: Python API only
- **Import Time**: 0.0002s (cached)

### finpull (Complete)
- **Purpose**: Desktop applications, command-line tools, data analysis
- **Size**: 27.2KB wheel, 188KB installed  
- **Dependencies**: All core dependencies + tkinter
- **Interfaces**: Python API + CLI + GUI
- **Import Time**: 0.0002s (cached)

## 💡 Key Features

### Core Features
- **27 Financial Metrics**: Comprehensive stock data from multiple sources
- **Multiple Interfaces**: API, CLI, and GUI for different use cases
- **Smart Validation**: Prevents invalid tickers with user-friendly error messages
- **Export Formats**: JSON, CSV, Excel with batch support
- **Progress Tracking**: Real-time status updates for all operations

## 🛠 Installation Guide

### For Web Developers
```bash
pip install finpull-core
```
Perfect for REST APIs, web scraping services, and embedded applications.

### For Data Analysts & Desktop Users
```bash
pip install finpull
```
Includes everything: API, CLI tools, and GUI application.

### For JavaScript Integration
JavaScript integration available via Pyodide (browser) and CLI commands (Node.js). See web integration section below.

## 📊 Usage Examples

### API Usage (Python)
```python
from finpull_core import FinancialDataAPI

# Initialize API
api = FinancialDataAPI()

# Add tickers
result = api.batch_add_tickers(['AAPL', 'MSFT', 'GOOGL'])
print(f"Added {result['summary']['added_count']} tickers")

# Get data
response = api.get_data('AAPL')
if response['success']:
    data = response['data']
    print(f"Apple Inc: ${data['price']} (P/E: {data['pe_ratio']})")

# Export data
api.export_data('json', 'portfolio.json')
```

### CLI Usage (Terminal)
```bash
# Add multiple tickers
finpull add AAPL MSFT GOOGL TSLA

# Show portfolio summary
finpull show

# Show detailed view
finpull show --full

# Refresh all data
finpull refresh

# Export to multiple formats
finpull export portfolio --json --csv --xlsx

# Get statistics
finpull stats

# Interactive mode
finpull --interactive
```

### GUI Usage (Desktop)
```bash
# Launch GUI
finpull --gui

# Or simply
finpull
```

Features:
- Add/remove tickers with validation
- Multi-selection for batch operations
- Sortable columns by any metric
- Export to multiple formats

## 🔧 Advanced Configuration

### Custom Storage Location
```python
from finpull_core import FinancialDataScraper

# Custom storage file
scraper = FinancialDataScraper(storage_file='/path/to/custom/data.json')
```

### Progress Callbacks
```python
def progress_callback(ticker, status):
    print(f"{ticker}: {status}")

api.refresh_data_with_progress(progress_callback=progress_callback)
```

### Data Validation
```python
# Validate before adding
if api.validate_ticker('AAPL')['valid']:
    api.add_ticker('AAPL')
```

## 📈 Data Coverage

Each ticker provides 27 comprehensive financial metrics including price, valuation ratios, earnings data, profitability metrics, growth indicators, financial health data, and trading statistics.

## 🌐 Web Integration

### Browser Usage (Pyodide)
```html
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
</head>
<body>
    <script>
        async function loadFinPull() {
            let pyodide = await loadPyodide();
            await pyodide.loadPackage("micropip");
            await pyodide.runPython(`
                import micropip
                await micropip.install('finpull-core')
                from finpull_core import FinancialDataAPI
                api = FinancialDataAPI()
            `);
            
            // Now use FinPull in browser
            pyodide.runPython(`
                api.add_ticker('AAPL')
                data = api.get_data('AAPL')
                print(f"Apple: ${data['data']['price']}")
            `);
        }
        loadFinPull();
    </script>
</body>
</html>
```

### Node.js Integration
```javascript
const { spawn } = require('child_process');

class FinPullJS {
    async addTicker(ticker) {
        return new Promise((resolve, reject) => {
            const process = spawn('finpull', ['add', ticker]);
            process.on('close', (code) => {
                resolve(code === 0);
            });
        });
    }
    
    async getData() {
        return new Promise((resolve, reject) => {
            const process = spawn('finpull', ['export', '--json', '/tmp/data.json']);
            process.on('close', (code) => {
                if (code === 0) {
                    const data = require('/tmp/data.json');
                    resolve(data);
                } else {
                    reject(new Error('Export failed'));
                }
            });
        });
    }
}
```

## 🚀 Performance Benchmarks

**Package Sizes**
- finpull-core: 21.9KB wheel → 134KB installed
- finpull: 27.2KB wheel → 188KB installed

**Import Performance**
- finpull-core: 0.0002s (cached)
- finpull: 0.0002s (cached)
- Cold start: ~0.9s (dependency loading)

**Data Fetching**
- Single ticker: ~1 second
- Batch operations: ~1 second per ticker
- Rate limiting: 1 second between requests

## 🔍 Troubleshooting

### Common Issues

**Import Errors**
```bash
# Ensure packages are installed
pip install --upgrade finpull-core
pip install --upgrade finpull
```

**GUI Won't Launch**
```bash
# Check display environment
echo $DISPLAY

# Install GUI dependencies (Linux)
sudo apt-get install python3-tk
```

**Network Issues**
```python
# Check data sources
from finpull_core import FinancialDataScraper
scraper = FinancialDataScraper()
print(scraper.get_stats()['data_sources'])
```

**Invalid Ticker Errors**
- Ensure ticker symbols are valid (e.g., 'AAPL' not 'Apple')
- Check for typos and proper formatting
- Some international tickers may not be supported

## 📚 Documentation

- **API Reference**: See `packages/finpull-core/docs/API_REFERENCE.md`
- **Interface Guide**: See `packages/finpull/docs/INTERFACES.md`

### Development Setup
```bash
git clone https://github.com/yourusername/finpull.git
cd finpull

# Install both packages in development mode
pip install -e packages/finpull-core/
pip install -e packages/finpull/

# Run tests
python -m pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


---
