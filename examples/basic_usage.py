#!/usr/bin/env python3
"""
Basic usage example for FinScraper
"""

import sys
import os

# Add the src directory to the path to import finscraper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from finscraper import FinancialDataScraper

def main():
    # Create scraper instance
    print("Creating FinScraper instance...")
    scraper = FinancialDataScraper()
    
    # Add some popular tickers
    tickers = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
    print(f"Adding tickers: {', '.join(tickers)}")
    
    for ticker in tickers:
        try:
            if scraper.add_ticker(ticker):
                print(f"✓ Added {ticker}")
            else:
                print(f"! {ticker} already exists")
        except Exception as e:
            print(f"✗ Error adding {ticker}: {e}")
    
    # Display all data
    print("\n=== Current Data ===")
    data_list = scraper.get_all_data()
    
    if data_list:
        for data in data_list:
            print(f"{data.ticker}: {data.company_name} - ${data.price} (P/E: {data.pe_ratio})")
    else:
        print("No data available")
    
    # Export data
    print("\n=== Exporting Data ===")
    try:
        json_file = scraper.export_data("json")
        print(f"✓ JSON export: {json_file}")
        
        csv_file = scraper.export_data("csv")
        print(f"✓ CSV export: {csv_file}")
        
        # Try Excel export if available
        try:
            xlsx_file = scraper.export_data("xlsx")
            print(f"✓ Excel export: {xlsx_file}")
        except ValueError as e:
            print(f"! Excel export not available: {e}")
            
    except Exception as e:
        print(f"✗ Export error: {e}")
    
    # Show statistics
    print("\n=== Statistics ===")
    stats = scraper.get_stats()
    print(f"Total tickers: {stats['total_tickers']}")
    print(f"Cached data: {stats['cached_tickers']}")
    print(f"Data sources: {stats['source_count']}")

if __name__ == "__main__":
    main() 