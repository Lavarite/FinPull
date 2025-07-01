#!/usr/bin/env python3
"""
API usage example for FinScraper
Demonstrates programmatic interface usage
"""

import sys
import os
import json

# Add the src directory to the path to import finscraper
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from finscraper import FinancialDataAPI

def main():
    print("=== FinScraper API Usage Example ===\n")
    
    # Create API instance
    api = FinancialDataAPI()
    
    # Add individual tickers
    print("Adding tickers...")
    tickers = ["AAPL", "GOOGL", "MSFT"]
    
    for ticker in tickers:
        result = api.add_ticker(ticker)
        if result["success"]:
            print(f"✓ {result['message']}")
        else:
            print(f"✗ {result.get('error', 'Unknown error')}")
    
    # Batch add tickers
    print("\nBatch adding tickers...")
    batch_tickers = ["AMZN", "TSLA", "META", "NVDA"]
    batch_result = api.batch_add_tickers(batch_tickers)
    
    print(f"Batch results:")
    print(f"  Added: {len(batch_result['added'])}")
    print(f"  Failed: {len(batch_result['failed'])}")
    print(f"  Already exists: {len(batch_result['already_exists'])}")
    
    if batch_result['failed']:
        print("  Failed tickers:")
        for failed in batch_result['failed']:
            print(f"    {failed['ticker']}: {failed['error']}")
    
    # Get ticker list
    print("\nGetting ticker list...")
    ticker_list_result = api.get_ticker_list()
    if ticker_list_result["success"]:
        print(f"Currently tracking {ticker_list_result['count']} tickers:")
        print(f"  {', '.join(ticker_list_result['tickers'])}")
    
    # Get all data
    print("\nRetrieving all data...")
    data_result = api.get_data()
    if data_result["success"]:
        print(f"Retrieved data for {data_result['count']} tickers:")
        for data in data_result["data"]:
            ticker = data.get("ticker", "N/A")
            company = data.get("company_name", "N/A")
            price = data.get("price", "N/A")
            pe_ratio = data.get("pe_ratio", "N/A")
            print(f"  {ticker}: {company} - ${price} (P/E: {pe_ratio})")
    
    # Get specific ticker data
    print("\nGetting specific ticker data...")
    specific_result = api.get_data("AAPL")
    if specific_result["success"] and specific_result["data"]:
        aapl_data = specific_result["data"]
        print(f"AAPL Details:")
        print(f"  Company: {aapl_data.get('company_name', 'N/A')}")
        print(f"  Sector: {aapl_data.get('sector', 'N/A')}")
        print(f"  Price: ${aapl_data.get('price', 'N/A')}")
        print(f"  Market Cap: {aapl_data.get('market_cap', 'N/A')}")
        print(f"  P/E Ratio: {aapl_data.get('pe_ratio', 'N/A')}")
    
    # Validate ticker
    print("\nValidating ticker symbols...")
    test_tickers = ["AAPL", "INVALID123", "GOOGL", "BADTICKER"]
    for ticker in test_tickers:
        validation_result = api.validate_ticker(ticker)
        if validation_result["success"]:
            status = "✓" if validation_result["valid"] else "✗"
            print(f"  {status} {ticker}")
    
    # Export data
    print("\nExporting data...")
    export_formats = ["json", "csv"]
    
    for format_type in export_formats:
        export_result = api.export_data(format_type)
        if export_result["success"]:
            print(f"✓ Exported {format_type.upper()}: {export_result['filename']}")
        else:
            print(f"✗ Export {format_type.upper()} failed: {export_result.get('error', 'Unknown error')}")
    
    # Get statistics
    print("\nGetting statistics...")
    stats_result = api.get_stats()
    if stats_result["success"]:
        stats = stats_result["stats"]
        print(f"Statistics:")
        print(f"  Total tickers: {stats.get('total_tickers', 0)}")
        print(f"  Cached tickers: {stats.get('cached_tickers', 0)}")
        print(f"  Data sources: {stats.get('source_count', 0)}")
        print(f"  Storage file: {stats.get('storage_file', 'N/A')}")
    
    # Demonstrate error handling
    print("\nDemonstrating error handling...")
    error_result = api.add_ticker("")  # Invalid ticker
    if not error_result["success"]:
        print(f"✓ Properly handled error: {error_result.get('error', 'Unknown error')}")
    
    # Cleanup stale data
    print("\nCleaning up stale data...")
    cleanup_result = api.cleanup_stale_data(24)  # 24 hours
    if cleanup_result["success"]:
        print(f"✓ {cleanup_result['message']}")
    
    print("\n=== API Usage Example Complete ===")

if __name__ == "__main__":
    main() 