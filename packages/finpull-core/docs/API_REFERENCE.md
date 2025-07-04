# FinPull Core API Reference

## Table of Contents

- [FinancialDataAPI Class](#financialdataapi-class)
- [FinancialDataScraper Class](#financialdatascraper-class)
- [FinancialData Class](#financialdata-class)
- [Data Format](#data-format)
- [Error Handling](#error-handling)

## FinancialDataAPI Class

The main interface for all financial data operations.

### Constructor

```python
FinancialDataAPI(storage_file: Optional[str] = None)
```

**Parameters:**
- `storage_file`: Optional custom path for data storage file

**Example:**
```python
from finpull_core import FinancialDataAPI

# Default storage location
api = FinancialDataAPI()

# Custom storage location
api = FinancialDataAPI(storage_file="/path/to/custom/storage.json")
```

### Methods

#### add_ticker(ticker: str) -> Dict[str, Any]

Add a ticker symbol for tracking.

**Parameters:**
- `ticker`: Stock ticker symbol (e.g., "AAPL")

**Returns:**
- Dictionary with success status and message

**Response Format:**
```json
{
    "success": true,
    "message": "Added AAPL",
    "ticker": "AAPL"
}
```

**Example:**
```python
result = api.add_ticker("AAPL")
if result['success']:
    print(f"Successfully added {result['ticker']}")
```

#### get_data(ticker: Optional[str] = None) -> Dict[str, Any]

Retrieve financial data for specific ticker or all tickers.

**Parameters:**
- `ticker`: Optional ticker symbol. If None, returns all data

**Returns:**
- Dictionary containing financial data

**Response Format (Single Ticker):**
```json
{
    "success": true,
    "data": {
        "ticker": "AAPL",
        "company_name": "Apple Inc.",
        "price": "150.00",
        // ... additional fields
    }
}
```

**Response Format (All Tickers):**
```json
{
    "success": true,
    "count": 3,
    "data": [
        {
            "ticker": "AAPL",
            "company_name": "Apple Inc.",
            // ... data fields
        },
        // ... additional tickers
    ]
}
```

**Example:**
```python
# Get specific ticker
data = api.get_data("AAPL")
if data['success']:
    stock_info = data['data']
    print(f"Price: ${stock_info['price']}")

# Get all tickers
all_data = api.get_data()
print(f"Tracking {all_data['count']} companies")
```

#### refresh_data(ticker: Optional[str] = None) -> Dict[str, Any]

Refresh financial data from external sources.

**Parameters:**
- `ticker`: Optional ticker symbol. If None, refreshes all data

**Returns:**
- Dictionary with operation status

**Response Format:**
```json
{
    "success": true,
    "message": "Refreshed 3 tickers",
    "refreshed_count": 3,
    "failed_count": 0
}
```

**Example:**
```python
# Refresh specific ticker
result = api.refresh_data("AAPL")

# Refresh all tickers
result = api.refresh_data()
print(f"Refreshed {result['refreshed_count']} tickers")
```

#### remove_ticker(ticker: str) -> Dict[str, Any]

Remove a ticker from tracking.

**Parameters:**
- `ticker`: Ticker symbol to remove

**Returns:**
- Dictionary with operation status

**Response Format:**
```json
{
    "success": true,
    "message": "Removed AAPL",
    "ticker": "AAPL"
}
```

**Example:**
```python
result = api.remove_ticker("AAPL")
if result['success']:
    print(f"Removed {result['ticker']}")
```

#### export_data(format_type: str = "json", filename: Optional[str] = None) -> Dict[str, Any]

Export tracked data to file.

**Parameters:**
- `format_type`: Export format ("json" or "csv")
- `filename`: Optional custom filename

**Returns:**
- Dictionary with export status and filename

**Response Format:**
```json
{
    "success": true,
    "message": "Data exported successfully",
    "filename": "finpull_data_20231201_123456.json",
    "format": "json",
    "record_count": 5
}
```

**Example:**
```python
# Export to JSON
result = api.export_data("json", "portfolio.json")

# Export to CSV with auto-generated filename
result = api.export_data("csv")
print(f"Exported to {result['filename']}")
```

#### validate_ticker(ticker: str) -> Dict[str, Any]

Validate ticker symbol format.

**Parameters:**
- `ticker`: Ticker symbol to validate

**Returns:**
- Dictionary with validation result

**Response Format:**
```json
{
    "success": true,
    "valid": true,
    "ticker": "AAPL",
    "message": "Valid ticker format"
}
```

**Example:**
```python
result = api.validate_ticker("AAPL")
if result['valid']:
    print(f"{result['ticker']} is valid")
```

#### get_stats() -> Dict[str, Any]

Get statistics about tracked data.

**Returns:**
- Dictionary with statistics

**Response Format:**
```json
{
    "success": true,
    "total_tickers": 5,
    "sectors": {
        "Technology": 3,
        "Healthcare": 2
    },
    "last_refresh": "2023-12-01T12:34:56",
    "storage_size": "2.5KB"
}
```

**Example:**
```python
stats = api.get_stats()
print(f"Tracking {stats['total_tickers']} tickers")
```

#### batch_add_tickers(tickers: List[str]) -> Dict[str, Any]

Add multiple tickers in a single operation.

**Parameters:**
- `tickers`: List of ticker symbols

**Returns:**
- Dictionary with batch operation results

**Response Format:**
```json
{
    "success": true,
    "summary": {
        "total_requested": 5,
        "added_count": 4,
        "failed_count": 1,
        "already_exists_count": 0
    },
    "results": [
        {
            "ticker": "AAPL",
            "success": true,
            "message": "Added successfully"
        },
        {
            "ticker": "INVALID",
            "success": false,
            "error": "Invalid ticker format"
        }
    ]
}
```

**Example:**
```python
tickers = ["AAPL", "GOOGL", "MSFT", "TSLA"]
results = api.batch_add_tickers(tickers)
print(f"Added {results['summary']['added_count']} out of {results['summary']['total_requested']} tickers")
```

## FinancialDataScraper Class

Lower-level interface for direct scraper operations.

### Constructor

```python
FinancialDataScraper(storage_file: Optional[str] = None)
```

### Key Methods

#### add_ticker(ticker: str) -> None

Add a ticker to the scraper.

**Parameters:**
- `ticker`: Stock ticker symbol

**Example:**
```python
from finpull_core import FinancialDataScraper

scraper = FinancialDataScraper()
scraper.add_ticker("AAPL")
```

#### get_ticker_data(ticker: str) -> Optional[FinancialData]

Get financial data for a specific ticker.

**Parameters:**
- `ticker`: Stock ticker symbol

**Returns:**
- FinancialData object or None if not found

**Example:**
```python
data = scraper.get_ticker_data("AAPL")
if data:
    print(f"Price: ${data.price}")
```

#### get_all_data() -> List[FinancialData]

Get all tracked financial data.

**Returns:**
- List of FinancialData objects

**Example:**
```python
all_data = scraper.get_all_data()
for stock in all_data:
    print(f"{stock.ticker}: ${stock.price}")
```

## FinancialData Class

Data model representing financial information.

### Attributes

All attributes are strings unless otherwise noted:

- `ticker`: Stock ticker symbol
- `company_name`: Company name
- `sector`: Business sector
- `price`: Current stock price
- `market_cap`: Market capitalization
- `pe_ratio`: Price-to-earnings ratio
- `pb_ratio`: Price-to-book ratio
- `ps_ratio`: Price-to-sales ratio
- `eps_ttm`: Earnings per share (trailing twelve months)
- `eps_next_year`: Projected earnings per share (next year)
- `eps_next_5y`: Projected earnings growth (next 5 years)
- `dividend_yield`: Dividend yield percentage
- `dividend_ttm`: Dividend per share (trailing twelve months)
- `revenue`: Total revenue
- `revenue_growth_5y`: Revenue growth (5 years)
- `operating_margin`: Operating margin percentage
- `profit_margin`: Profit margin percentage
- `roa`: Return on assets percentage
- `roe`: Return on equity percentage
- `roi`: Return on investment percentage
- `total_assets`: Total company assets
- `total_liabilities`: Total company liabilities
- `change_5y`: Stock price change (5 years)
- `beta`: Beta coefficient
- `volume`: Current trading volume
- `avg_volume`: Average trading volume
- `timestamp`: Data timestamp (ISO format)

### Methods

#### to_dict() -> Dict[str, str]

Convert to dictionary format.

**Returns:**
- Dictionary with all financial data

**Example:**
```python
data = scraper.get_ticker_data("AAPL")
dict_data = data.to_dict()
print(dict_data['company_name'])
```

## Data Format

All financial data follows this consistent structure:

```json
{
    "ticker": "AAPL",
    "company_name": "Apple Inc.",
    "sector": "Technology",
    "price": "150.00",
    "market_cap": "2.5T",
    "pe_ratio": "25.5",
    "pb_ratio": "8.2",
    "ps_ratio": "7.1",
    "eps_ttm": "5.89",
    "eps_next_year": "6.15",
    "eps_next_5y": "8.2%",
    "dividend_yield": "0.5%",
    "dividend_ttm": "0.92",
    "revenue": "394.3B",
    "revenue_growth_5y": "9.1%",
    "operating_margin": "30.3%",
    "profit_margin": "25.7%",
    "roa": "20.1%",
    "roe": "147.4%",
    "roi": "29.2%",
    "total_assets": "352.8B",
    "total_liabilities": "287.9B",
    "change_5y": "245.6%",
    "beta": "1.2",
    "volume": "50.2M",
    "avg_volume": "58.4M",
    "timestamp": "2023-12-01T12:34:56"
}
```

### Data Sources

1. **Finviz** (Primary): Comprehensive financial metrics and ratios
2. **Yahoo Finance** (Fallback): Real-time pricing and market data

## Error Handling

All API methods return consistent error responses:

### Success Response
```json
{
    "success": true,
    "data": { /* response data */ }
}
```

### Error Response
```json
{
    "success": false,
    "error": "Error message",
    "error_code": "INVALID_TICKER"
}
```

### Common Error Codes

- `INVALID_TICKER`: Ticker format is invalid
- `TICKER_NOT_FOUND`: Ticker not found in tracking
- `NETWORK_ERROR`: Unable to fetch data from sources
- `STORAGE_ERROR`: File system access error
- `RATE_LIMIT_EXCEEDED`: Too many requests

### Exception Handling

```python
try:
    result = api.add_ticker("AAPL")
    if not result['success']:
        print(f"Error: {result['error']}")
except Exception as e:
    print(f"Unexpected error: {e}") 