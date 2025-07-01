# FinScraper Examples

This directory contains example scripts demonstrating different ways to use FinScraper.

## Running the Examples

From the FinScraper root directory:

```bash
python examples/basic_usage.py
python examples/batch_processing.py
python examples/api_usage.py
```

## Example Scripts

### basic_usage.py
Demonstrates basic FinScraper usage:
- Creating a scraper instance
- Adding tickers
- Retrieving data
- Exporting to different formats
- Viewing statistics

### batch_processing.py
Shows batch processing capabilities:
- Fetching multiple tickers at once
- Performance analysis across different sectors
- Summary statistics generation

### api_usage.py
Demonstrates programmatic API usage:
- Using the FinancialDataAPI class
- Batch operations
- Error handling
- Data validation
- Export operations

## Integration Examples

### As a Library
```python
from finscraper import FinancialDataScraper

scraper = FinancialDataScraper()
scraper.add_ticker("AAPL")
data = scraper.get_all_data()
```

### Batch Processing
```python
from finscraper.utils.batch import batch_fetch_tickers

tickers = ["AAPL", "GOOGL", "MSFT"]
results = batch_fetch_tickers(tickers)
```

### Web/API Integration
```python
from finscraper import FinancialDataAPI

api = FinancialDataAPI()
result = api.add_ticker("AAPL")
```

## Tips

1. **Error Handling**: Always wrap operations in try-catch blocks for production use
2. **Rate Limiting**: The scraper automatically handles rate limiting
3. **Data Persistence**: Data is automatically saved between sessions
4. **Mock Data**: If external APIs fail, mock data is provided for testing 